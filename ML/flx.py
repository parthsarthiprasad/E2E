import tensorflow as tf
import numpy as np

img_crop = 3

#Figure out the tf concrete function problem

def repeat(x, num_repeats):
    with tf.name_scope("repeat"):
        ones = tf.ones((1, num_repeats), dtype='int32')
        x = tf.reshape(x, shape=(-1,1))
        x = tf.matmul(x, ones)
        return tf.reshape(x, [-1])

def interpolate(image, x, y, output_size):
    with tf.name_scope("interpolate"):
        batch_size = tf.shape(image)[0]
        height = tf.shape(image)[1]
        width = tf.shape(image)[2]
        num_channels = tf.shape(image)[3]

        x = tf.cast(x , dtype='float32')
        y = tf.cast(y , dtype='float32')

        height_float = tf.cast(height, dtype='float32')
        width_float = tf.cast(width, dtype='float32')

        output_height = output_size[0]
        output_width  = output_size[1]

        x = .5*(x + 1.0)*(width_float)
        y = .5*(y + 1.0)*(height_float)

        x0 = tf.cast(tf.floor(x), 'int32')
        x1 = x0 + 1
        y0 = tf.cast(tf.floor(y), 'int32')
        y1 = y0 + 1

        max_y = tf.cast(height - 1, dtype='int32')
        max_x = tf.cast(width - 1,  dtype='int32')
        zero = tf.zeros([], dtype='int32')

        x0 = tf.clip_by_value(x0, zero, max_x)
        x1 = tf.clip_by_value(x1, zero, max_x)
        y0 = tf.clip_by_value(y0, zero, max_y)
        y1 = tf.clip_by_value(y1, zero, max_y)

        flat_image_dimensions = height*width
        pixels_batch = tf.range(batch_size)*flat_image_dimensions
        flat_output_dimensions = output_height*output_width
        base = repeat(pixels_batch, flat_output_dimensions)
        base_y0 = base + y0*width
        base_y1 = base + y1*width
        indices_a = base_y0 + x0
        indices_b = base_y1 + x0
        indices_c = base_y0 + x1
        indices_d = base_y1 + x1

        flat_image = tf.reshape(image, shape=(-1, num_channels))
        flat_image = tf.cast(flat_image, dtype='float32')
        pixel_values_a = tf.gather(flat_image, indices_a)
        pixel_values_b = tf.gather(flat_image, indices_b)
        pixel_values_c = tf.gather(flat_image, indices_c)
        pixel_values_d = tf.gather(flat_image, indices_d)

        x0 = tf.cast(x0, 'float32')
        x1 = tf.cast(x1, 'float32')
        y0 = tf.cast(y0, 'float32')
        y1 = tf.cast(y1, 'float32')

        area_a = tf.expand_dims(((x1 - x) * (y1 - y)), 1)
        area_b = tf.expand_dims(((x1 - x) * (y - y0)), 1)
        area_c = tf.expand_dims(((x - x0) * (y1 - y)), 1)
        area_d = tf.expand_dims(((x - x0) * (y - y0)), 1)
        output = tf.add_n([area_a*pixel_values_a,
                           area_b*pixel_values_b,
                           area_c*pixel_values_c,
                           area_d*pixel_values_d])
        return output

def meshgrid(height, width):
    with tf.name_scope("meshgrid"):
        y_linspace = tf.linspace(-1., 1., height)
        x_linspace = tf.linspace(-1., 1., width)
        x_coordinates, y_coordinates = tf.meshgrid(x_linspace, y_linspace)    
        y_coordinates = tf.expand_dims(tf.reshape(y_coordinates, [-1]),0)
        x_coordinates = tf.expand_dims(tf.reshape(x_coordinates, [-1]),0)
        indices_grid = tf.concat([x_coordinates, y_coordinates], 0)
        return indices_grid

def apply_transformation(flows, img, num_channels):
    with tf.name_scope("apply_transformation"):
        batch_size = tf.shape(img)[0]
        height = tf.shape(img)[1]
        width = tf.shape(img)[2]
        # num_channels = tf.shape(img)[3]
        output_size = (height, width)
        flow_channels = tf.shape(flows)[3]

        flows = tf.reshape(tf.transpose(flows, [0, 3, 1, 2]), [batch_size, flow_channels, height*width])

        indices_grid = meshgrid(height, width)

        transformed_grid = tf.add(flows, indices_grid)
        x_s = tf.slice(transformed_grid, [0, 0, 0], [-1, 1, -1])
        y_s = tf.slice(transformed_grid, [0, 1, 0], [-1, 1, -1])
        x_s_flatten = tf.reshape(x_s, [-1])
        y_s_flatten = tf.reshape(y_s, [-1])

        transformed_image = interpolate(img, x_s_flatten, y_s_flatten, (height, width))

        transformed_image = tf.reshape(transformed_image, [batch_size, height, width, num_channels])
        return transformed_image

def batch_norm(x, train_phase, name='bn_layer'):
    #with tf.variable_scope(name) as scope:
    batch_norm = tf.layers.batch_normalization(
            inputs=x,
            momentum=0.9, epsilon=1e-5,
            center=True, scale=True,
            training = train_phase,
            name=name)
    return batch_norm
    
def cnn_blk(inputs, filters, kernel_size, phase_train, name = 'cnn_blk'):
    with tf.variable_scope(name) as scope:
        cnn = tf.layers.conv2d(inputs=inputs, filters=filters, kernel_size=kernel_size, padding="same", activation=None, use_bias=False, name="cnn")
        act = tf.nn.relu(cnn, name= "act")
        ret = batch_norm(act, phase_train)
        return ret

def dnn_blk(inputs, nodes, name = 'dnn_blk'):
    with tf.variable_scope(name) as scope:
        dnn = tf.layers.dense(inputs=inputs, units=nodes, activation=None, name="dnn")
        ret = tf.nn.relu(dnn, name= "act")
        return ret

def gen_agl_map(inputs, height, width,feature_dims):
    with tf.name_scope("gen_agl_map"):
        batch_size = tf.shape(inputs)[0]
        ret = tf.reshape(tf.tile(inputs,tf.constant([1,height*width])), [batch_size,height,width,feature_dims])
        return ret

def encoder(inputs, height, width, tar_dim):
    with tf.variable_scope('encoder'):
        dnn_blk_0 =  dnn_blk(inputs, 16, name = 'dnn_blk_0')
        dnn_blk_1 =  dnn_blk(dnn_blk_0, 16, name = 'dnn_blk_1')
        dnn_blk_2 =  dnn_blk(dnn_blk_1, tar_dim, name = 'dnn_blk_2')
        agl_map = gen_agl_map(dnn_blk_2, height, width, tar_dim)
        return agl_map

def apply_lcm(batch_img, light_weight):
    with tf.name_scope('apply_lcm'):
        img_wgts, pal_wgts = tf.split(light_weight, [1,1], 3)
        img_wgts = tf.tile(img_wgts, [1,1,1,3])
        pal_wgts = tf.tile(pal_wgts, [1,1,1,3])
        palette = tf.ones(tf.shape(batch_img), dtype = tf.float32)
        ret = tf.add(tf.multiply(batch_img, img_wgts), tf.multiply(palette, pal_wgts))
        return ret
    
def trans_module(inputs, structures, phase_train, name="trans_module"):
    with tf.variable_scope(name) as scope:
        cnn_blk_0 = cnn_blk(inputs, structures['depth'][0], structures['filter_size'][0], phase_train, name = 'cnn_blk_0')
        cnn_blk_1 = cnn_blk(cnn_blk_0, structures['depth'][1], structures['filter_size'][1], phase_train, name = 'cnn_blk_1')
        cnn_blk_2 = cnn_blk(tf.concat([cnn_blk_0,cnn_blk_1], axis=3), structures['depth'][2], structures['filter_size'][2], phase_train, name = 'cnn_blk_2')
        cnn_blk_3 = cnn_blk(tf.concat([cnn_blk_0,cnn_blk_1,cnn_blk_2], axis=3), structures['depth'][3], structures['filter_size'][3], phase_train, name = 'cnn_blk_3')
        cnn_4 = tf.layers.conv2d(inputs=cnn_blk_3, filters=structures['depth'][4], kernel_size=structures['filter_size'][4], padding="same", activation=None, use_bias=False, name="cnn_4")
        return cnn_4
    
def lcm_module(inputs, structures, phase_train, name="lcm_module"):
    with tf.variable_scope(name) as scope:
        cnn_blk_0 = cnn_blk(inputs, structures['depth'][0], structures['filter_size'][0], phase_train, name = 'cnn_blk_0')        
        cnn_blk_1 = cnn_blk(cnn_blk_0, structures['depth'][1], structures['filter_size'][1], phase_train, name = 'cnn_blk_1')
        cnn_2 = tf.layers.conv2d(inputs=cnn_blk_1, filters=structures['depth'][2], kernel_size=structures['filter_size'][2], padding="same", activation=None, use_bias=False, name='cnn_2')
        lcm_map = tf.nn.softmax(cnn_2)
        return lcm_map

def inference(input_img, input_fp, input_agl, phase_train, conf):
    """Build the Deepwarp model.
    Args: images, anchors_map of eye, angle 
    Returns: lcm images
    """
    corse_layer = {'depth':(32,64,64,32,16), 'filter_size':([5,5],[3,3],[3,3],[3,3],[1,1])}
    fine_layer = {'depth':(32,64,32,16,4), 'filter_size':([5,5],[3,3],[3,3],[3,3],[1,1])}
    lcm_layer = {'depth':(8,8,2), 'filter_size':([3,3],[3,3],[1,1])}
    
    with tf.variable_scope('warping_model'):        
        agl_map = encoder(input_agl, conf.height, conf.width, conf.encoded_agl_dim)        
        igt_inputs = tf.concat([input_img, input_fp, agl_map],axis=3)
        
        with tf.variable_scope('warping_module'):
            '''coarse module'''
            resized_igt_inputs = tf.layers.average_pooling2d(inputs=igt_inputs, pool_size=[2,2], strides=2, padding='same')
            cours_raw = trans_module(resized_igt_inputs, corse_layer, phase_train, name='coarse_level')
            cours_act = tf.nn.tanh(cours_raw)
            coarse_resize = tf.image.resize_images(cours_act, (conf.height, conf.width), method=tf.image.ResizeMethod.NEAREST_NEIGHBOR)
            coarse_out = tf.layers.average_pooling2d(inputs=coarse_resize, pool_size=[2, 2], strides=1, padding='same')
            '''fine module'''
            fine_input = tf.concat([igt_inputs, coarse_out],axis=3, name='fine_input')
            fine_out = trans_module(fine_input, fine_layer, phase_train, name='fine_level')
            flow_raw, lcm_input = tf.split(fine_out, [2,2], 3)

        flow = tf.nn.tanh(flow_raw)
        cfw_img = apply_transformation(flows = flow, img = input_img, num_channels=3)
        '''lcm module'''
        lcm_map = lcm_module(lcm_input, lcm_layer, phase_train, name="lcm_module")
        img_pred = apply_lcm(batch_img=cfw_img, light_weight=lcm_map)

        return img_pred, flow_raw, lcm_map
