node {
  name: "inputs/input_img"
  op: "Placeholder"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: -1
        }
        dim {
          size: 48
        }
        dim {
          size: 64
        }
        dim {
          size: 3
        }
      }
    }
  }
}
node {
  name: "inputs/input_fp"
  op: "Placeholder"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: -1
        }
        dim {
          size: 48
        }
        dim {
          size: 64
        }
        dim {
          size: 12
        }
      }
    }
  }
}
node {
  name: "inputs/input_ang"
  op: "Placeholder"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: -1
        }
        dim {
          size: 2
        }
      }
    }
  }
}
node {
  name: "inputs/phase_train"
  op: "Placeholder"
  attr {
    key: "dtype"
    value {
      type: DT_BOOL
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        unknown_rank: true
      }
    }
  }
}
node {
  name: "warping_model/encoder/dnn_blk_0/dnn/kernel/Initializer/random_uniform/shape"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/encoder/dnn_blk_0/dnn/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 2
          }
        }
        tensor_content: "\002\000\000\000\020\000\000\000"
      }
    }
  }
}
node {
  name: "warping_model/encoder/dnn_blk_0/dnn/kernel/Initializer/random_uniform/min"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/encoder/dnn_blk_0/dnn/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: -0.5773502588272095
      }
    }
  }
}
node {
  name: "warping_model/encoder/dnn_blk_0/dnn/kernel/Initializer/random_uniform/max"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/encoder/dnn_blk_0/dnn/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 0.5773502588272095
      }
    }
  }
}
node {
  name: "warping_model/encoder/dnn_blk_0/dnn/kernel/Initializer/random_uniform/RandomUniform"
  op: "RandomUniform"
  input: "warping_model/encoder/dnn_blk_0/dnn/kernel/Initializer/random_uniform/shape"
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/encoder/dnn_blk_0/dnn/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "seed"
    value {
      i: 0
    }
  }
  attr {
    key: "seed2"
    value {
      i: 0
    }
  }
}
node {
  name: "warping_model/encoder/dnn_blk_0/dnn/kernel/Initializer/random_uniform/sub"
  op: "Sub"
  input: "warping_model/encoder/dnn_blk_0/dnn/kernel/Initializer/random_uniform/max"
  input: "warping_model/encoder/dnn_blk_0/dnn/kernel/Initializer/random_uniform/min"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/encoder/dnn_blk_0/dnn/kernel"
      }
    }
  }
}
node {
  name: "warping_model/encoder/dnn_blk_0/dnn/kernel/Initializer/random_uniform/mul"
  op: "Mul"
  input: "warping_model/encoder/dnn_blk_0/dnn/kernel/Initializer/random_uniform/RandomUniform"
  input: "warping_model/encoder/dnn_blk_0/dnn/kernel/Initializer/random_uniform/sub"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/encoder/dnn_blk_0/dnn/kernel"
      }
    }
  }
}
node {
  name: "warping_model/encoder/dnn_blk_0/dnn/kernel/Initializer/random_uniform"
  op: "Add"
  input: "warping_model/encoder/dnn_blk_0/dnn/kernel/Initializer/random_uniform/mul"
  input: "warping_model/encoder/dnn_blk_0/dnn/kernel/Initializer/random_uniform/min"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/encoder/dnn_blk_0/dnn/kernel"
      }
    }
  }
}
node {
  name: "warping_model/encoder/dnn_blk_0/dnn/kernel"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/encoder/dnn_blk_0/dnn/kernel"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 2
        }
        dim {
          size: 16
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/encoder/dnn_blk_0/dnn/kernel/Assign"
  op: "Assign"
  input: "warping_model/encoder/dnn_blk_0/dnn/kernel"
  input: "warping_model/encoder/dnn_blk_0/dnn/kernel/Initializer/random_uniform"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/encoder/dnn_blk_0/dnn/kernel"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/encoder/dnn_blk_0/dnn/kernel/read"
  op: "Identity"
  input: "warping_model/encoder/dnn_blk_0/dnn/kernel"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/encoder/dnn_blk_0/dnn/kernel"
      }
    }
  }
}
node {
  name: "warping_model/encoder/dnn_blk_0/dnn/bias/Initializer/zeros"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/encoder/dnn_blk_0/dnn/bias"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 16
          }
        }
        float_val: 0.0
      }
    }
  }
}
node {
  name: "warping_model/encoder/dnn_blk_0/dnn/bias"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/encoder/dnn_blk_0/dnn/bias"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 16
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/encoder/dnn_blk_0/dnn/bias/Assign"
  op: "Assign"
  input: "warping_model/encoder/dnn_blk_0/dnn/bias"
  input: "warping_model/encoder/dnn_blk_0/dnn/bias/Initializer/zeros"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/encoder/dnn_blk_0/dnn/bias"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/encoder/dnn_blk_0/dnn/bias/read"
  op: "Identity"
  input: "warping_model/encoder/dnn_blk_0/dnn/bias"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/encoder/dnn_blk_0/dnn/bias"
      }
    }
  }
}
node {
  name: "warping_model/encoder/dnn_blk_0/dnn/MatMul"
  op: "MatMul"
  input: "inputs/input_ang"
  input: "warping_model/encoder/dnn_blk_0/dnn/kernel/read"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "transpose_a"
    value {
      b: false
    }
  }
  attr {
    key: "transpose_b"
    value {
      b: false
    }
  }
}
node {
  name: "warping_model/encoder/dnn_blk_0/dnn/BiasAdd"
  op: "BiasAdd"
  input: "warping_model/encoder/dnn_blk_0/dnn/MatMul"
  input: "warping_model/encoder/dnn_blk_0/dnn/bias/read"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "data_format"
    value {
      s: "NHWC"
    }
  }
}
node {
  name: "warping_model/encoder/dnn_blk_0/act"
  op: "Relu"
  input: "warping_model/encoder/dnn_blk_0/dnn/BiasAdd"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/encoder/dnn_blk_1/dnn/kernel/Initializer/random_uniform/shape"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/encoder/dnn_blk_1/dnn/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 2
          }
        }
        tensor_content: "\020\000\000\000\020\000\000\000"
      }
    }
  }
}
node {
  name: "warping_model/encoder/dnn_blk_1/dnn/kernel/Initializer/random_uniform/min"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/encoder/dnn_blk_1/dnn/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: -0.4330126941204071
      }
    }
  }
}
node {
  name: "warping_model/encoder/dnn_blk_1/dnn/kernel/Initializer/random_uniform/max"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/encoder/dnn_blk_1/dnn/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 0.4330126941204071
      }
    }
  }
}
node {
  name: "warping_model/encoder/dnn_blk_1/dnn/kernel/Initializer/random_uniform/RandomUniform"
  op: "RandomUniform"
  input: "warping_model/encoder/dnn_blk_1/dnn/kernel/Initializer/random_uniform/shape"
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/encoder/dnn_blk_1/dnn/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "seed"
    value {
      i: 0
    }
  }
  attr {
    key: "seed2"
    value {
      i: 0
    }
  }
}
node {
  name: "warping_model/encoder/dnn_blk_1/dnn/kernel/Initializer/random_uniform/sub"
  op: "Sub"
  input: "warping_model/encoder/dnn_blk_1/dnn/kernel/Initializer/random_uniform/max"
  input: "warping_model/encoder/dnn_blk_1/dnn/kernel/Initializer/random_uniform/min"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/encoder/dnn_blk_1/dnn/kernel"
      }
    }
  }
}
node {
  name: "warping_model/encoder/dnn_blk_1/dnn/kernel/Initializer/random_uniform/mul"
  op: "Mul"
  input: "warping_model/encoder/dnn_blk_1/dnn/kernel/Initializer/random_uniform/RandomUniform"
  input: "warping_model/encoder/dnn_blk_1/dnn/kernel/Initializer/random_uniform/sub"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/encoder/dnn_blk_1/dnn/kernel"
      }
    }
  }
}
node {
  name: "warping_model/encoder/dnn_blk_1/dnn/kernel/Initializer/random_uniform"
  op: "Add"
  input: "warping_model/encoder/dnn_blk_1/dnn/kernel/Initializer/random_uniform/mul"
  input: "warping_model/encoder/dnn_blk_1/dnn/kernel/Initializer/random_uniform/min"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/encoder/dnn_blk_1/dnn/kernel"
      }
    }
  }
}
node {
  name: "warping_model/encoder/dnn_blk_1/dnn/kernel"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/encoder/dnn_blk_1/dnn/kernel"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 16
        }
        dim {
          size: 16
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/encoder/dnn_blk_1/dnn/kernel/Assign"
  op: "Assign"
  input: "warping_model/encoder/dnn_blk_1/dnn/kernel"
  input: "warping_model/encoder/dnn_blk_1/dnn/kernel/Initializer/random_uniform"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/encoder/dnn_blk_1/dnn/kernel"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/encoder/dnn_blk_1/dnn/kernel/read"
  op: "Identity"
  input: "warping_model/encoder/dnn_blk_1/dnn/kernel"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/encoder/dnn_blk_1/dnn/kernel"
      }
    }
  }
}
node {
  name: "warping_model/encoder/dnn_blk_1/dnn/bias/Initializer/zeros"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/encoder/dnn_blk_1/dnn/bias"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 16
          }
        }
        float_val: 0.0
      }
    }
  }
}
node {
  name: "warping_model/encoder/dnn_blk_1/dnn/bias"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/encoder/dnn_blk_1/dnn/bias"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 16
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/encoder/dnn_blk_1/dnn/bias/Assign"
  op: "Assign"
  input: "warping_model/encoder/dnn_blk_1/dnn/bias"
  input: "warping_model/encoder/dnn_blk_1/dnn/bias/Initializer/zeros"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/encoder/dnn_blk_1/dnn/bias"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/encoder/dnn_blk_1/dnn/bias/read"
  op: "Identity"
  input: "warping_model/encoder/dnn_blk_1/dnn/bias"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/encoder/dnn_blk_1/dnn/bias"
      }
    }
  }
}
node {
  name: "warping_model/encoder/dnn_blk_1/dnn/MatMul"
  op: "MatMul"
  input: "warping_model/encoder/dnn_blk_0/act"
  input: "warping_model/encoder/dnn_blk_1/dnn/kernel/read"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "transpose_a"
    value {
      b: false
    }
  }
  attr {
    key: "transpose_b"
    value {
      b: false
    }
  }
}
node {
  name: "warping_model/encoder/dnn_blk_1/dnn/BiasAdd"
  op: "BiasAdd"
  input: "warping_model/encoder/dnn_blk_1/dnn/MatMul"
  input: "warping_model/encoder/dnn_blk_1/dnn/bias/read"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "data_format"
    value {
      s: "NHWC"
    }
  }
}
node {
  name: "warping_model/encoder/dnn_blk_1/act"
  op: "Relu"
  input: "warping_model/encoder/dnn_blk_1/dnn/BiasAdd"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/encoder/dnn_blk_2/dnn/kernel/Initializer/random_uniform/shape"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/encoder/dnn_blk_2/dnn/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 2
          }
        }
        tensor_content: "\020\000\000\000\020\000\000\000"
      }
    }
  }
}
node {
  name: "warping_model/encoder/dnn_blk_2/dnn/kernel/Initializer/random_uniform/min"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/encoder/dnn_blk_2/dnn/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: -0.4330126941204071
      }
    }
  }
}
node {
  name: "warping_model/encoder/dnn_blk_2/dnn/kernel/Initializer/random_uniform/max"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/encoder/dnn_blk_2/dnn/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 0.4330126941204071
      }
    }
  }
}
node {
  name: "warping_model/encoder/dnn_blk_2/dnn/kernel/Initializer/random_uniform/RandomUniform"
  op: "RandomUniform"
  input: "warping_model/encoder/dnn_blk_2/dnn/kernel/Initializer/random_uniform/shape"
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/encoder/dnn_blk_2/dnn/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "seed"
    value {
      i: 0
    }
  }
  attr {
    key: "seed2"
    value {
      i: 0
    }
  }
}
node {
  name: "warping_model/encoder/dnn_blk_2/dnn/kernel/Initializer/random_uniform/sub"
  op: "Sub"
  input: "warping_model/encoder/dnn_blk_2/dnn/kernel/Initializer/random_uniform/max"
  input: "warping_model/encoder/dnn_blk_2/dnn/kernel/Initializer/random_uniform/min"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/encoder/dnn_blk_2/dnn/kernel"
      }
    }
  }
}
node {
  name: "warping_model/encoder/dnn_blk_2/dnn/kernel/Initializer/random_uniform/mul"
  op: "Mul"
  input: "warping_model/encoder/dnn_blk_2/dnn/kernel/Initializer/random_uniform/RandomUniform"
  input: "warping_model/encoder/dnn_blk_2/dnn/kernel/Initializer/random_uniform/sub"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/encoder/dnn_blk_2/dnn/kernel"
      }
    }
  }
}
node {
  name: "warping_model/encoder/dnn_blk_2/dnn/kernel/Initializer/random_uniform"
  op: "Add"
  input: "warping_model/encoder/dnn_blk_2/dnn/kernel/Initializer/random_uniform/mul"
  input: "warping_model/encoder/dnn_blk_2/dnn/kernel/Initializer/random_uniform/min"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/encoder/dnn_blk_2/dnn/kernel"
      }
    }
  }
}
node {
  name: "warping_model/encoder/dnn_blk_2/dnn/kernel"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/encoder/dnn_blk_2/dnn/kernel"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 16
        }
        dim {
          size: 16
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/encoder/dnn_blk_2/dnn/kernel/Assign"
  op: "Assign"
  input: "warping_model/encoder/dnn_blk_2/dnn/kernel"
  input: "warping_model/encoder/dnn_blk_2/dnn/kernel/Initializer/random_uniform"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/encoder/dnn_blk_2/dnn/kernel"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/encoder/dnn_blk_2/dnn/kernel/read"
  op: "Identity"
  input: "warping_model/encoder/dnn_blk_2/dnn/kernel"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/encoder/dnn_blk_2/dnn/kernel"
      }
    }
  }
}
node {
  name: "warping_model/encoder/dnn_blk_2/dnn/bias/Initializer/zeros"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/encoder/dnn_blk_2/dnn/bias"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 16
          }
        }
        float_val: 0.0
      }
    }
  }
}
node {
  name: "warping_model/encoder/dnn_blk_2/dnn/bias"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/encoder/dnn_blk_2/dnn/bias"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 16
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/encoder/dnn_blk_2/dnn/bias/Assign"
  op: "Assign"
  input: "warping_model/encoder/dnn_blk_2/dnn/bias"
  input: "warping_model/encoder/dnn_blk_2/dnn/bias/Initializer/zeros"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/encoder/dnn_blk_2/dnn/bias"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/encoder/dnn_blk_2/dnn/bias/read"
  op: "Identity"
  input: "warping_model/encoder/dnn_blk_2/dnn/bias"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/encoder/dnn_blk_2/dnn/bias"
      }
    }
  }
}
node {
  name: "warping_model/encoder/dnn_blk_2/dnn/MatMul"
  op: "MatMul"
  input: "warping_model/encoder/dnn_blk_1/act"
  input: "warping_model/encoder/dnn_blk_2/dnn/kernel/read"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "transpose_a"
    value {
      b: false
    }
  }
  attr {
    key: "transpose_b"
    value {
      b: false
    }
  }
}
node {
  name: "warping_model/encoder/dnn_blk_2/dnn/BiasAdd"
  op: "BiasAdd"
  input: "warping_model/encoder/dnn_blk_2/dnn/MatMul"
  input: "warping_model/encoder/dnn_blk_2/dnn/bias/read"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "data_format"
    value {
      s: "NHWC"
    }
  }
}
node {
  name: "warping_model/encoder/dnn_blk_2/act"
  op: "Relu"
  input: "warping_model/encoder/dnn_blk_2/dnn/BiasAdd"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/encoder/gen_agl_map/Shape"
  op: "Shape"
  input: "warping_model/encoder/dnn_blk_2/act"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "out_type"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/encoder/gen_agl_map/strided_slice/stack"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 1
          }
        }
        int_val: 0
      }
    }
  }
}
node {
  name: "warping_model/encoder/gen_agl_map/strided_slice/stack_1"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 1
          }
        }
        int_val: 1
      }
    }
  }
}
node {
  name: "warping_model/encoder/gen_agl_map/strided_slice/stack_2"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 1
          }
        }
        int_val: 1
      }
    }
  }
}
node {
  name: "warping_model/encoder/gen_agl_map/strided_slice"
  op: "StridedSlice"
  input: "warping_model/encoder/gen_agl_map/Shape"
  input: "warping_model/encoder/gen_agl_map/strided_slice/stack"
  input: "warping_model/encoder/gen_agl_map/strided_slice/stack_1"
  input: "warping_model/encoder/gen_agl_map/strided_slice/stack_2"
  attr {
    key: "Index"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "begin_mask"
    value {
      i: 0
    }
  }
  attr {
    key: "ellipsis_mask"
    value {
      i: 0
    }
  }
  attr {
    key: "end_mask"
    value {
      i: 0
    }
  }
  attr {
    key: "new_axis_mask"
    value {
      i: 0
    }
  }
  attr {
    key: "shrink_axis_mask"
    value {
      i: 1
    }
  }
}
node {
  name: "warping_model/encoder/gen_agl_map/Const"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 2
          }
        }
        tensor_content: "\001\000\000\000\000\014\000\000"
      }
    }
  }
}
node {
  name: "warping_model/encoder/gen_agl_map/Tile"
  op: "Tile"
  input: "warping_model/encoder/dnn_blk_2/act"
  input: "warping_model/encoder/gen_agl_map/Const"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "Tmultiples"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/encoder/gen_agl_map/Reshape/shape/1"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
        }
        int_val: 48
      }
    }
  }
}
node {
  name: "warping_model/encoder/gen_agl_map/Reshape/shape/2"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
        }
        int_val: 64
      }
    }
  }
}
node {
  name: "warping_model/encoder/gen_agl_map/Reshape/shape/3"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
        }
        int_val: 16
      }
    }
  }
}
node {
  name: "warping_model/encoder/gen_agl_map/Reshape/shape"
  op: "Pack"
  input: "warping_model/encoder/gen_agl_map/strided_slice"
  input: "warping_model/encoder/gen_agl_map/Reshape/shape/1"
  input: "warping_model/encoder/gen_agl_map/Reshape/shape/2"
  input: "warping_model/encoder/gen_agl_map/Reshape/shape/3"
  attr {
    key: "N"
    value {
      i: 4
    }
  }
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "axis"
    value {
      i: 0
    }
  }
}
node {
  name: "warping_model/encoder/gen_agl_map/Reshape"
  op: "Reshape"
  input: "warping_model/encoder/gen_agl_map/Tile"
  input: "warping_model/encoder/gen_agl_map/Reshape/shape"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "Tshape"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/concat/axis"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
        }
        int_val: 3
      }
    }
  }
}
node {
  name: "warping_model/concat"
  op: "ConcatV2"
  input: "inputs/input_img"
  input: "inputs/input_fp"
  input: "warping_model/encoder/gen_agl_map/Reshape"
  input: "warping_model/concat/axis"
  attr {
    key: "N"
    value {
      i: 3
    }
  }
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "Tidx"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/warping_module/average_pooling2d/AvgPool"
  op: "AvgPool"
  input: "warping_model/concat"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "data_format"
    value {
      s: "NHWC"
    }
  }
  attr {
    key: "ksize"
    value {
      list {
        i: 1
        i: 2
        i: 2
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 2
        i: 2
        i: 1
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/cnn/kernel/Initializer/random_uniform/shape"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_0/cnn/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 4
          }
        }
        tensor_content: "\005\000\000\000\005\000\000\000\037\000\000\000 \000\000\000"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/cnn/kernel/Initializer/random_uniform/min"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_0/cnn/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: -0.06172133982181549
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/cnn/kernel/Initializer/random_uniform/max"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_0/cnn/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 0.06172133982181549
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/cnn/kernel/Initializer/random_uniform/RandomUniform"
  op: "RandomUniform"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/cnn/kernel/Initializer/random_uniform/shape"
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_0/cnn/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "seed"
    value {
      i: 0
    }
  }
  attr {
    key: "seed2"
    value {
      i: 0
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/cnn/kernel/Initializer/random_uniform/sub"
  op: "Sub"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/cnn/kernel/Initializer/random_uniform/max"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/cnn/kernel/Initializer/random_uniform/min"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_0/cnn/kernel"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/cnn/kernel/Initializer/random_uniform/mul"
  op: "Mul"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/cnn/kernel/Initializer/random_uniform/RandomUniform"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/cnn/kernel/Initializer/random_uniform/sub"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_0/cnn/kernel"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/cnn/kernel/Initializer/random_uniform"
  op: "Add"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/cnn/kernel/Initializer/random_uniform/mul"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/cnn/kernel/Initializer/random_uniform/min"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_0/cnn/kernel"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/cnn/kernel"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_0/cnn/kernel"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 5
        }
        dim {
          size: 5
        }
        dim {
          size: 31
        }
        dim {
          size: 32
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/cnn/kernel/Assign"
  op: "Assign"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/cnn/kernel"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/cnn/kernel/Initializer/random_uniform"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_0/cnn/kernel"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/cnn/kernel/read"
  op: "Identity"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/cnn/kernel"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_0/cnn/kernel"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/cnn/dilation_rate"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 2
          }
        }
        tensor_content: "\001\000\000\000\001\000\000\000"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/cnn/Conv2D"
  op: "Conv2D"
  input: "warping_model/warping_module/average_pooling2d/AvgPool"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/cnn/kernel/read"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "data_format"
    value {
      s: "NHWC"
    }
  }
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "use_cudnn_on_gpu"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/act"
  op: "Relu"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/cnn/Conv2D"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/gamma/Initializer/ones"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/gamma"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 32
          }
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/gamma"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/gamma"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 32
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/gamma/Assign"
  op: "Assign"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/gamma"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/gamma/Initializer/ones"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/gamma"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/gamma/read"
  op: "Identity"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/gamma"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/gamma"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/beta/Initializer/zeros"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/beta"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 32
          }
        }
        float_val: 0.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/beta"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/beta"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 32
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/beta/Assign"
  op: "Assign"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/beta"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/beta/Initializer/zeros"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/beta"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/beta/read"
  op: "Identity"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/beta"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/beta"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/moving_mean/Initializer/zeros"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 32
          }
        }
        float_val: 0.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/moving_mean"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 32
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/moving_mean/Assign"
  op: "Assign"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/moving_mean"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/moving_mean/Initializer/zeros"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/moving_mean/read"
  op: "Identity"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/moving_mean"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/moving_mean"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/moving_variance/Initializer/ones"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 32
          }
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/moving_variance"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 32
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/moving_variance/Assign"
  op: "Assign"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/moving_variance"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/moving_variance/Initializer/ones"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/moving_variance/read"
  op: "Identity"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/moving_variance"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/moving_variance"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond/Switch"
  op: "Switch"
  input: "inputs/phase_train"
  input: "inputs/phase_train"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond/switch_t"
  op: "Identity"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond/Switch:1"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond/switch_f"
  op: "Identity"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond/Switch"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond/pred_id"
  op: "Identity"
  input: "inputs/phase_train"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond/Const"
  op: "Const"
  input: "^warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond/switch_t"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
          }
        }
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond/Const_1"
  op: "Const"
  input: "^warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond/switch_t"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
          }
        }
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond/FusedBatchNorm"
  op: "FusedBatchNorm"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond/FusedBatchNorm/Switch:1"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond/FusedBatchNorm/Switch_1:1"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond/FusedBatchNorm/Switch_2:1"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond/Const"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond/Const_1"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "data_format"
    value {
      s: "NHWC"
    }
  }
  attr {
    key: "epsilon"
    value {
      f: 1.0009999641624745e-05
    }
  }
  attr {
    key: "is_training"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond/FusedBatchNorm/Switch"
  op: "Switch"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/act"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_0/act"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond/FusedBatchNorm/Switch_1"
  op: "Switch"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/gamma/read"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/gamma"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond/FusedBatchNorm/Switch_2"
  op: "Switch"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/beta/read"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/beta"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond/FusedBatchNorm_1"
  op: "FusedBatchNorm"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond/FusedBatchNorm_1/Switch"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond/FusedBatchNorm_1/Switch_1"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond/FusedBatchNorm_1/Switch_2"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond/FusedBatchNorm_1/Switch_3"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond/FusedBatchNorm_1/Switch_4"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "data_format"
    value {
      s: "NHWC"
    }
  }
  attr {
    key: "epsilon"
    value {
      f: 1.0009999641624745e-05
    }
  }
  attr {
    key: "is_training"
    value {
      b: false
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond/FusedBatchNorm_1/Switch"
  op: "Switch"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/act"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_0/act"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond/FusedBatchNorm_1/Switch_1"
  op: "Switch"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/gamma/read"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/gamma"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond/FusedBatchNorm_1/Switch_2"
  op: "Switch"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/beta/read"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/beta"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond/FusedBatchNorm_1/Switch_3"
  op: "Switch"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/moving_mean/read"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/moving_mean"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond/FusedBatchNorm_1/Switch_4"
  op: "Switch"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/moving_variance/read"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/moving_variance"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond/Merge"
  op: "Merge"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond/FusedBatchNorm_1"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond/FusedBatchNorm"
  attr {
    key: "N"
    value {
      i: 2
    }
  }
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond/Merge_1"
  op: "Merge"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond/FusedBatchNorm_1:1"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond/FusedBatchNorm:1"
  attr {
    key: "N"
    value {
      i: 2
    }
  }
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond/Merge_2"
  op: "Merge"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond/FusedBatchNorm_1:2"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond/FusedBatchNorm:2"
  attr {
    key: "N"
    value {
      i: 2
    }
  }
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond_1/Switch"
  op: "Switch"
  input: "inputs/phase_train"
  input: "inputs/phase_train"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond_1/switch_t"
  op: "Identity"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond_1/Switch:1"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond_1/switch_f"
  op: "Identity"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond_1/Switch"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond_1/pred_id"
  op: "Identity"
  input: "inputs/phase_train"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond_1/Const"
  op: "Const"
  input: "^warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond_1/switch_t"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 0.8999999761581421
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond_1/Const_1"
  op: "Const"
  input: "^warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond_1/switch_f"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond_1/Merge"
  op: "Merge"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond_1/Const_1"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond_1/Const"
  attr {
    key: "N"
    value {
      i: 2
    }
  }
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/AssignMovingAvg/sub/x"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/AssignMovingAvg/sub"
  op: "Sub"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/AssignMovingAvg/sub/x"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond_1/Merge"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/moving_mean"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/AssignMovingAvg/sub_1"
  op: "Sub"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/moving_mean/read"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond/Merge_1"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/moving_mean"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/AssignMovingAvg/mul"
  op: "Mul"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/AssignMovingAvg/sub_1"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/AssignMovingAvg/sub"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/moving_mean"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/AssignMovingAvg"
  op: "AssignSub"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/moving_mean"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/AssignMovingAvg/mul"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: false
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/AssignMovingAvg_1/sub/x"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/AssignMovingAvg_1/sub"
  op: "Sub"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/AssignMovingAvg_1/sub/x"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond_1/Merge"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/moving_variance"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/AssignMovingAvg_1/sub_1"
  op: "Sub"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/moving_variance/read"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond/Merge_2"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/moving_variance"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/AssignMovingAvg_1/mul"
  op: "Mul"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/AssignMovingAvg_1/sub_1"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/AssignMovingAvg_1/sub"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/moving_variance"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/AssignMovingAvg_1"
  op: "AssignSub"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/moving_variance"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/AssignMovingAvg_1/mul"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: false
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/cnn/kernel/Initializer/random_uniform/shape"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_1/cnn/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 4
          }
        }
        tensor_content: "\003\000\000\000\003\000\000\000 \000\000\000@\000\000\000"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/cnn/kernel/Initializer/random_uniform/min"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_1/cnn/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: -0.0833333358168602
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/cnn/kernel/Initializer/random_uniform/max"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_1/cnn/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 0.0833333358168602
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/cnn/kernel/Initializer/random_uniform/RandomUniform"
  op: "RandomUniform"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/cnn/kernel/Initializer/random_uniform/shape"
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_1/cnn/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "seed"
    value {
      i: 0
    }
  }
  attr {
    key: "seed2"
    value {
      i: 0
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/cnn/kernel/Initializer/random_uniform/sub"
  op: "Sub"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/cnn/kernel/Initializer/random_uniform/max"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/cnn/kernel/Initializer/random_uniform/min"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_1/cnn/kernel"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/cnn/kernel/Initializer/random_uniform/mul"
  op: "Mul"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/cnn/kernel/Initializer/random_uniform/RandomUniform"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/cnn/kernel/Initializer/random_uniform/sub"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_1/cnn/kernel"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/cnn/kernel/Initializer/random_uniform"
  op: "Add"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/cnn/kernel/Initializer/random_uniform/mul"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/cnn/kernel/Initializer/random_uniform/min"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_1/cnn/kernel"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/cnn/kernel"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_1/cnn/kernel"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 3
        }
        dim {
          size: 3
        }
        dim {
          size: 32
        }
        dim {
          size: 64
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/cnn/kernel/Assign"
  op: "Assign"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/cnn/kernel"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/cnn/kernel/Initializer/random_uniform"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_1/cnn/kernel"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/cnn/kernel/read"
  op: "Identity"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/cnn/kernel"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_1/cnn/kernel"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/cnn/dilation_rate"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 2
          }
        }
        tensor_content: "\001\000\000\000\001\000\000\000"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/cnn/Conv2D"
  op: "Conv2D"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond/Merge"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/cnn/kernel/read"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "data_format"
    value {
      s: "NHWC"
    }
  }
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "use_cudnn_on_gpu"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/act"
  op: "Relu"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/cnn/Conv2D"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/gamma/Initializer/ones"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/gamma"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 64
          }
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/gamma"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/gamma"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 64
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/gamma/Assign"
  op: "Assign"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/gamma"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/gamma/Initializer/ones"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/gamma"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/gamma/read"
  op: "Identity"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/gamma"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/gamma"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/beta/Initializer/zeros"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/beta"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 64
          }
        }
        float_val: 0.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/beta"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/beta"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 64
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/beta/Assign"
  op: "Assign"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/beta"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/beta/Initializer/zeros"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/beta"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/beta/read"
  op: "Identity"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/beta"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/beta"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/moving_mean/Initializer/zeros"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 64
          }
        }
        float_val: 0.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/moving_mean"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 64
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/moving_mean/Assign"
  op: "Assign"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/moving_mean"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/moving_mean/Initializer/zeros"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/moving_mean/read"
  op: "Identity"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/moving_mean"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/moving_mean"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/moving_variance/Initializer/ones"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 64
          }
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/moving_variance"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 64
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/moving_variance/Assign"
  op: "Assign"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/moving_variance"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/moving_variance/Initializer/ones"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/moving_variance/read"
  op: "Identity"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/moving_variance"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/moving_variance"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond/Switch"
  op: "Switch"
  input: "inputs/phase_train"
  input: "inputs/phase_train"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond/switch_t"
  op: "Identity"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond/Switch:1"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond/switch_f"
  op: "Identity"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond/Switch"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond/pred_id"
  op: "Identity"
  input: "inputs/phase_train"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond/Const"
  op: "Const"
  input: "^warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond/switch_t"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
          }
        }
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond/Const_1"
  op: "Const"
  input: "^warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond/switch_t"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
          }
        }
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond/FusedBatchNorm"
  op: "FusedBatchNorm"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond/FusedBatchNorm/Switch:1"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond/FusedBatchNorm/Switch_1:1"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond/FusedBatchNorm/Switch_2:1"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond/Const"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond/Const_1"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "data_format"
    value {
      s: "NHWC"
    }
  }
  attr {
    key: "epsilon"
    value {
      f: 1.0009999641624745e-05
    }
  }
  attr {
    key: "is_training"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond/FusedBatchNorm/Switch"
  op: "Switch"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/act"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_1/act"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond/FusedBatchNorm/Switch_1"
  op: "Switch"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/gamma/read"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/gamma"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond/FusedBatchNorm/Switch_2"
  op: "Switch"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/beta/read"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/beta"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond/FusedBatchNorm_1"
  op: "FusedBatchNorm"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond/FusedBatchNorm_1/Switch"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond/FusedBatchNorm_1/Switch_1"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond/FusedBatchNorm_1/Switch_2"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond/FusedBatchNorm_1/Switch_3"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond/FusedBatchNorm_1/Switch_4"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "data_format"
    value {
      s: "NHWC"
    }
  }
  attr {
    key: "epsilon"
    value {
      f: 1.0009999641624745e-05
    }
  }
  attr {
    key: "is_training"
    value {
      b: false
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond/FusedBatchNorm_1/Switch"
  op: "Switch"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/act"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_1/act"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond/FusedBatchNorm_1/Switch_1"
  op: "Switch"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/gamma/read"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/gamma"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond/FusedBatchNorm_1/Switch_2"
  op: "Switch"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/beta/read"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/beta"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond/FusedBatchNorm_1/Switch_3"
  op: "Switch"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/moving_mean/read"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/moving_mean"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond/FusedBatchNorm_1/Switch_4"
  op: "Switch"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/moving_variance/read"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/moving_variance"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond/Merge"
  op: "Merge"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond/FusedBatchNorm_1"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond/FusedBatchNorm"
  attr {
    key: "N"
    value {
      i: 2
    }
  }
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond/Merge_1"
  op: "Merge"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond/FusedBatchNorm_1:1"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond/FusedBatchNorm:1"
  attr {
    key: "N"
    value {
      i: 2
    }
  }
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond/Merge_2"
  op: "Merge"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond/FusedBatchNorm_1:2"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond/FusedBatchNorm:2"
  attr {
    key: "N"
    value {
      i: 2
    }
  }
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond_1/Switch"
  op: "Switch"
  input: "inputs/phase_train"
  input: "inputs/phase_train"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond_1/switch_t"
  op: "Identity"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond_1/Switch:1"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond_1/switch_f"
  op: "Identity"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond_1/Switch"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond_1/pred_id"
  op: "Identity"
  input: "inputs/phase_train"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond_1/Const"
  op: "Const"
  input: "^warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond_1/switch_t"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 0.8999999761581421
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond_1/Const_1"
  op: "Const"
  input: "^warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond_1/switch_f"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond_1/Merge"
  op: "Merge"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond_1/Const_1"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond_1/Const"
  attr {
    key: "N"
    value {
      i: 2
    }
  }
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/AssignMovingAvg/sub/x"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/AssignMovingAvg/sub"
  op: "Sub"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/AssignMovingAvg/sub/x"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond_1/Merge"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/moving_mean"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/AssignMovingAvg/sub_1"
  op: "Sub"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/moving_mean/read"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond/Merge_1"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/moving_mean"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/AssignMovingAvg/mul"
  op: "Mul"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/AssignMovingAvg/sub_1"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/AssignMovingAvg/sub"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/moving_mean"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/AssignMovingAvg"
  op: "AssignSub"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/moving_mean"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/AssignMovingAvg/mul"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: false
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/AssignMovingAvg_1/sub/x"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/AssignMovingAvg_1/sub"
  op: "Sub"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/AssignMovingAvg_1/sub/x"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond_1/Merge"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/moving_variance"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/AssignMovingAvg_1/sub_1"
  op: "Sub"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/moving_variance/read"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond/Merge_2"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/moving_variance"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/AssignMovingAvg_1/mul"
  op: "Mul"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/AssignMovingAvg_1/sub_1"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/AssignMovingAvg_1/sub"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/moving_variance"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/AssignMovingAvg_1"
  op: "AssignSub"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/moving_variance"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/AssignMovingAvg_1/mul"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: false
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/concat/axis"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
        }
        int_val: 3
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/concat"
  op: "ConcatV2"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond/Merge"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond/Merge"
  input: "warping_model/warping_module/coarse_level/concat/axis"
  attr {
    key: "N"
    value {
      i: 2
    }
  }
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "Tidx"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/cnn/kernel/Initializer/random_uniform/shape"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_2/cnn/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 4
          }
        }
        tensor_content: "\003\000\000\000\003\000\000\000`\000\000\000@\000\000\000"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/cnn/kernel/Initializer/random_uniform/min"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_2/cnn/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: -0.06454972177743912
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/cnn/kernel/Initializer/random_uniform/max"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_2/cnn/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 0.06454972177743912
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/cnn/kernel/Initializer/random_uniform/RandomUniform"
  op: "RandomUniform"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/cnn/kernel/Initializer/random_uniform/shape"
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_2/cnn/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "seed"
    value {
      i: 0
    }
  }
  attr {
    key: "seed2"
    value {
      i: 0
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/cnn/kernel/Initializer/random_uniform/sub"
  op: "Sub"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/cnn/kernel/Initializer/random_uniform/max"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/cnn/kernel/Initializer/random_uniform/min"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_2/cnn/kernel"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/cnn/kernel/Initializer/random_uniform/mul"
  op: "Mul"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/cnn/kernel/Initializer/random_uniform/RandomUniform"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/cnn/kernel/Initializer/random_uniform/sub"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_2/cnn/kernel"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/cnn/kernel/Initializer/random_uniform"
  op: "Add"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/cnn/kernel/Initializer/random_uniform/mul"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/cnn/kernel/Initializer/random_uniform/min"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_2/cnn/kernel"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/cnn/kernel"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_2/cnn/kernel"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 3
        }
        dim {
          size: 3
        }
        dim {
          size: 96
        }
        dim {
          size: 64
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/cnn/kernel/Assign"
  op: "Assign"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/cnn/kernel"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/cnn/kernel/Initializer/random_uniform"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_2/cnn/kernel"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/cnn/kernel/read"
  op: "Identity"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/cnn/kernel"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_2/cnn/kernel"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/cnn/dilation_rate"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 2
          }
        }
        tensor_content: "\001\000\000\000\001\000\000\000"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/cnn/Conv2D"
  op: "Conv2D"
  input: "warping_model/warping_module/coarse_level/concat"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/cnn/kernel/read"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "data_format"
    value {
      s: "NHWC"
    }
  }
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "use_cudnn_on_gpu"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/act"
  op: "Relu"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/cnn/Conv2D"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/gamma/Initializer/ones"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/gamma"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 64
          }
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/gamma"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/gamma"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 64
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/gamma/Assign"
  op: "Assign"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/gamma"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/gamma/Initializer/ones"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/gamma"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/gamma/read"
  op: "Identity"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/gamma"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/gamma"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/beta/Initializer/zeros"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/beta"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 64
          }
        }
        float_val: 0.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/beta"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/beta"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 64
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/beta/Assign"
  op: "Assign"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/beta"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/beta/Initializer/zeros"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/beta"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/beta/read"
  op: "Identity"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/beta"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/beta"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/moving_mean/Initializer/zeros"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 64
          }
        }
        float_val: 0.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/moving_mean"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 64
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/moving_mean/Assign"
  op: "Assign"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/moving_mean"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/moving_mean/Initializer/zeros"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/moving_mean/read"
  op: "Identity"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/moving_mean"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/moving_mean"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/moving_variance/Initializer/ones"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 64
          }
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/moving_variance"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 64
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/moving_variance/Assign"
  op: "Assign"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/moving_variance"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/moving_variance/Initializer/ones"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/moving_variance/read"
  op: "Identity"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/moving_variance"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/moving_variance"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond/Switch"
  op: "Switch"
  input: "inputs/phase_train"
  input: "inputs/phase_train"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond/switch_t"
  op: "Identity"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond/Switch:1"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond/switch_f"
  op: "Identity"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond/Switch"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond/pred_id"
  op: "Identity"
  input: "inputs/phase_train"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond/Const"
  op: "Const"
  input: "^warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond/switch_t"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
          }
        }
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond/Const_1"
  op: "Const"
  input: "^warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond/switch_t"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
          }
        }
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond/FusedBatchNorm"
  op: "FusedBatchNorm"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond/FusedBatchNorm/Switch:1"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond/FusedBatchNorm/Switch_1:1"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond/FusedBatchNorm/Switch_2:1"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond/Const"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond/Const_1"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "data_format"
    value {
      s: "NHWC"
    }
  }
  attr {
    key: "epsilon"
    value {
      f: 1.0009999641624745e-05
    }
  }
  attr {
    key: "is_training"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond/FusedBatchNorm/Switch"
  op: "Switch"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/act"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_2/act"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond/FusedBatchNorm/Switch_1"
  op: "Switch"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/gamma/read"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/gamma"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond/FusedBatchNorm/Switch_2"
  op: "Switch"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/beta/read"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/beta"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond/FusedBatchNorm_1"
  op: "FusedBatchNorm"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond/FusedBatchNorm_1/Switch"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond/FusedBatchNorm_1/Switch_1"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond/FusedBatchNorm_1/Switch_2"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond/FusedBatchNorm_1/Switch_3"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond/FusedBatchNorm_1/Switch_4"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "data_format"
    value {
      s: "NHWC"
    }
  }
  attr {
    key: "epsilon"
    value {
      f: 1.0009999641624745e-05
    }
  }
  attr {
    key: "is_training"
    value {
      b: false
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond/FusedBatchNorm_1/Switch"
  op: "Switch"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/act"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_2/act"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond/FusedBatchNorm_1/Switch_1"
  op: "Switch"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/gamma/read"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/gamma"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond/FusedBatchNorm_1/Switch_2"
  op: "Switch"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/beta/read"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/beta"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond/FusedBatchNorm_1/Switch_3"
  op: "Switch"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/moving_mean/read"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/moving_mean"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond/FusedBatchNorm_1/Switch_4"
  op: "Switch"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/moving_variance/read"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/moving_variance"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond/Merge"
  op: "Merge"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond/FusedBatchNorm_1"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond/FusedBatchNorm"
  attr {
    key: "N"
    value {
      i: 2
    }
  }
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond/Merge_1"
  op: "Merge"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond/FusedBatchNorm_1:1"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond/FusedBatchNorm:1"
  attr {
    key: "N"
    value {
      i: 2
    }
  }
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond/Merge_2"
  op: "Merge"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond/FusedBatchNorm_1:2"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond/FusedBatchNorm:2"
  attr {
    key: "N"
    value {
      i: 2
    }
  }
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond_1/Switch"
  op: "Switch"
  input: "inputs/phase_train"
  input: "inputs/phase_train"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond_1/switch_t"
  op: "Identity"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond_1/Switch:1"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond_1/switch_f"
  op: "Identity"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond_1/Switch"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond_1/pred_id"
  op: "Identity"
  input: "inputs/phase_train"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond_1/Const"
  op: "Const"
  input: "^warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond_1/switch_t"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 0.8999999761581421
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond_1/Const_1"
  op: "Const"
  input: "^warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond_1/switch_f"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond_1/Merge"
  op: "Merge"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond_1/Const_1"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond_1/Const"
  attr {
    key: "N"
    value {
      i: 2
    }
  }
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/AssignMovingAvg/sub/x"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/AssignMovingAvg/sub"
  op: "Sub"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/AssignMovingAvg/sub/x"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond_1/Merge"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/moving_mean"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/AssignMovingAvg/sub_1"
  op: "Sub"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/moving_mean/read"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond/Merge_1"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/moving_mean"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/AssignMovingAvg/mul"
  op: "Mul"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/AssignMovingAvg/sub_1"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/AssignMovingAvg/sub"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/moving_mean"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/AssignMovingAvg"
  op: "AssignSub"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/moving_mean"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/AssignMovingAvg/mul"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: false
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/AssignMovingAvg_1/sub/x"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/AssignMovingAvg_1/sub"
  op: "Sub"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/AssignMovingAvg_1/sub/x"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond_1/Merge"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/moving_variance"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/AssignMovingAvg_1/sub_1"
  op: "Sub"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/moving_variance/read"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond/Merge_2"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/moving_variance"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/AssignMovingAvg_1/mul"
  op: "Mul"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/AssignMovingAvg_1/sub_1"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/AssignMovingAvg_1/sub"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/moving_variance"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/AssignMovingAvg_1"
  op: "AssignSub"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/moving_variance"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/AssignMovingAvg_1/mul"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: false
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/concat_1/axis"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
        }
        int_val: 3
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/concat_1"
  op: "ConcatV2"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/cond/Merge"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/cond/Merge"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/cond/Merge"
  input: "warping_model/warping_module/coarse_level/concat_1/axis"
  attr {
    key: "N"
    value {
      i: 3
    }
  }
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "Tidx"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/cnn/kernel/Initializer/random_uniform/shape"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_3/cnn/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 4
          }
        }
        tensor_content: "\003\000\000\000\003\000\000\000\240\000\000\000 \000\000\000"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/cnn/kernel/Initializer/random_uniform/min"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_3/cnn/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: -0.0589255653321743
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/cnn/kernel/Initializer/random_uniform/max"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_3/cnn/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 0.0589255653321743
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/cnn/kernel/Initializer/random_uniform/RandomUniform"
  op: "RandomUniform"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/cnn/kernel/Initializer/random_uniform/shape"
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_3/cnn/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "seed"
    value {
      i: 0
    }
  }
  attr {
    key: "seed2"
    value {
      i: 0
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/cnn/kernel/Initializer/random_uniform/sub"
  op: "Sub"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/cnn/kernel/Initializer/random_uniform/max"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/cnn/kernel/Initializer/random_uniform/min"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_3/cnn/kernel"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/cnn/kernel/Initializer/random_uniform/mul"
  op: "Mul"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/cnn/kernel/Initializer/random_uniform/RandomUniform"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/cnn/kernel/Initializer/random_uniform/sub"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_3/cnn/kernel"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/cnn/kernel/Initializer/random_uniform"
  op: "Add"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/cnn/kernel/Initializer/random_uniform/mul"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/cnn/kernel/Initializer/random_uniform/min"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_3/cnn/kernel"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/cnn/kernel"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_3/cnn/kernel"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 3
        }
        dim {
          size: 3
        }
        dim {
          size: 160
        }
        dim {
          size: 32
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/cnn/kernel/Assign"
  op: "Assign"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/cnn/kernel"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/cnn/kernel/Initializer/random_uniform"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_3/cnn/kernel"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/cnn/kernel/read"
  op: "Identity"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/cnn/kernel"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_3/cnn/kernel"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/cnn/dilation_rate"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 2
          }
        }
        tensor_content: "\001\000\000\000\001\000\000\000"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/cnn/Conv2D"
  op: "Conv2D"
  input: "warping_model/warping_module/coarse_level/concat_1"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/cnn/kernel/read"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "data_format"
    value {
      s: "NHWC"
    }
  }
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "use_cudnn_on_gpu"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/act"
  op: "Relu"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/cnn/Conv2D"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/gamma/Initializer/ones"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/gamma"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 32
          }
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/gamma"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/gamma"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 32
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/gamma/Assign"
  op: "Assign"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/gamma"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/gamma/Initializer/ones"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/gamma"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/gamma/read"
  op: "Identity"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/gamma"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/gamma"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/beta/Initializer/zeros"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/beta"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 32
          }
        }
        float_val: 0.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/beta"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/beta"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 32
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/beta/Assign"
  op: "Assign"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/beta"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/beta/Initializer/zeros"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/beta"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/beta/read"
  op: "Identity"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/beta"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/beta"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/moving_mean/Initializer/zeros"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 32
          }
        }
        float_val: 0.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/moving_mean"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 32
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/moving_mean/Assign"
  op: "Assign"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/moving_mean"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/moving_mean/Initializer/zeros"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/moving_mean/read"
  op: "Identity"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/moving_mean"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/moving_mean"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/moving_variance/Initializer/ones"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 32
          }
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/moving_variance"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 32
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/moving_variance/Assign"
  op: "Assign"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/moving_variance"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/moving_variance/Initializer/ones"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/moving_variance/read"
  op: "Identity"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/moving_variance"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/moving_variance"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond/Switch"
  op: "Switch"
  input: "inputs/phase_train"
  input: "inputs/phase_train"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond/switch_t"
  op: "Identity"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond/Switch:1"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond/switch_f"
  op: "Identity"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond/Switch"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond/pred_id"
  op: "Identity"
  input: "inputs/phase_train"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond/Const"
  op: "Const"
  input: "^warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond/switch_t"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
          }
        }
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond/Const_1"
  op: "Const"
  input: "^warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond/switch_t"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
          }
        }
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond/FusedBatchNorm"
  op: "FusedBatchNorm"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond/FusedBatchNorm/Switch:1"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond/FusedBatchNorm/Switch_1:1"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond/FusedBatchNorm/Switch_2:1"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond/Const"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond/Const_1"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "data_format"
    value {
      s: "NHWC"
    }
  }
  attr {
    key: "epsilon"
    value {
      f: 1.0009999641624745e-05
    }
  }
  attr {
    key: "is_training"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond/FusedBatchNorm/Switch"
  op: "Switch"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/act"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_3/act"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond/FusedBatchNorm/Switch_1"
  op: "Switch"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/gamma/read"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/gamma"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond/FusedBatchNorm/Switch_2"
  op: "Switch"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/beta/read"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/beta"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond/FusedBatchNorm_1"
  op: "FusedBatchNorm"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond/FusedBatchNorm_1/Switch"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond/FusedBatchNorm_1/Switch_1"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond/FusedBatchNorm_1/Switch_2"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond/FusedBatchNorm_1/Switch_3"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond/FusedBatchNorm_1/Switch_4"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "data_format"
    value {
      s: "NHWC"
    }
  }
  attr {
    key: "epsilon"
    value {
      f: 1.0009999641624745e-05
    }
  }
  attr {
    key: "is_training"
    value {
      b: false
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond/FusedBatchNorm_1/Switch"
  op: "Switch"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/act"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_3/act"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond/FusedBatchNorm_1/Switch_1"
  op: "Switch"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/gamma/read"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/gamma"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond/FusedBatchNorm_1/Switch_2"
  op: "Switch"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/beta/read"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/beta"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond/FusedBatchNorm_1/Switch_3"
  op: "Switch"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/moving_mean/read"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/moving_mean"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond/FusedBatchNorm_1/Switch_4"
  op: "Switch"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/moving_variance/read"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/moving_variance"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond/Merge"
  op: "Merge"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond/FusedBatchNorm_1"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond/FusedBatchNorm"
  attr {
    key: "N"
    value {
      i: 2
    }
  }
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond/Merge_1"
  op: "Merge"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond/FusedBatchNorm_1:1"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond/FusedBatchNorm:1"
  attr {
    key: "N"
    value {
      i: 2
    }
  }
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond/Merge_2"
  op: "Merge"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond/FusedBatchNorm_1:2"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond/FusedBatchNorm:2"
  attr {
    key: "N"
    value {
      i: 2
    }
  }
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond_1/Switch"
  op: "Switch"
  input: "inputs/phase_train"
  input: "inputs/phase_train"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond_1/switch_t"
  op: "Identity"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond_1/Switch:1"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond_1/switch_f"
  op: "Identity"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond_1/Switch"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond_1/pred_id"
  op: "Identity"
  input: "inputs/phase_train"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond_1/Const"
  op: "Const"
  input: "^warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond_1/switch_t"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 0.8999999761581421
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond_1/Const_1"
  op: "Const"
  input: "^warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond_1/switch_f"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond_1/Merge"
  op: "Merge"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond_1/Const_1"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond_1/Const"
  attr {
    key: "N"
    value {
      i: 2
    }
  }
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/AssignMovingAvg/sub/x"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/AssignMovingAvg/sub"
  op: "Sub"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/AssignMovingAvg/sub/x"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond_1/Merge"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/moving_mean"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/AssignMovingAvg/sub_1"
  op: "Sub"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/moving_mean/read"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond/Merge_1"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/moving_mean"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/AssignMovingAvg/mul"
  op: "Mul"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/AssignMovingAvg/sub_1"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/AssignMovingAvg/sub"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/moving_mean"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/AssignMovingAvg"
  op: "AssignSub"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/moving_mean"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/AssignMovingAvg/mul"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: false
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/AssignMovingAvg_1/sub/x"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/AssignMovingAvg_1/sub"
  op: "Sub"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/AssignMovingAvg_1/sub/x"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond_1/Merge"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/moving_variance"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/AssignMovingAvg_1/sub_1"
  op: "Sub"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/moving_variance/read"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond/Merge_2"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/moving_variance"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/AssignMovingAvg_1/mul"
  op: "Mul"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/AssignMovingAvg_1/sub_1"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/AssignMovingAvg_1/sub"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/moving_variance"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/AssignMovingAvg_1"
  op: "AssignSub"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/moving_variance"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/AssignMovingAvg_1/mul"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: false
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_4/kernel/Initializer/random_uniform/shape"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_4/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 4
          }
        }
        tensor_content: "\001\000\000\000\001\000\000\000 \000\000\000\020\000\000\000"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_4/kernel/Initializer/random_uniform/min"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_4/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: -0.3535533845424652
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_4/kernel/Initializer/random_uniform/max"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_4/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 0.3535533845424652
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_4/kernel/Initializer/random_uniform/RandomUniform"
  op: "RandomUniform"
  input: "warping_model/warping_module/coarse_level/cnn_4/kernel/Initializer/random_uniform/shape"
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_4/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "seed"
    value {
      i: 0
    }
  }
  attr {
    key: "seed2"
    value {
      i: 0
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_4/kernel/Initializer/random_uniform/sub"
  op: "Sub"
  input: "warping_model/warping_module/coarse_level/cnn_4/kernel/Initializer/random_uniform/max"
  input: "warping_model/warping_module/coarse_level/cnn_4/kernel/Initializer/random_uniform/min"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_4/kernel"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_4/kernel/Initializer/random_uniform/mul"
  op: "Mul"
  input: "warping_model/warping_module/coarse_level/cnn_4/kernel/Initializer/random_uniform/RandomUniform"
  input: "warping_model/warping_module/coarse_level/cnn_4/kernel/Initializer/random_uniform/sub"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_4/kernel"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_4/kernel/Initializer/random_uniform"
  op: "Add"
  input: "warping_model/warping_module/coarse_level/cnn_4/kernel/Initializer/random_uniform/mul"
  input: "warping_model/warping_module/coarse_level/cnn_4/kernel/Initializer/random_uniform/min"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_4/kernel"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_4/kernel"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_4/kernel"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 1
        }
        dim {
          size: 1
        }
        dim {
          size: 32
        }
        dim {
          size: 16
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_4/kernel/Assign"
  op: "Assign"
  input: "warping_model/warping_module/coarse_level/cnn_4/kernel"
  input: "warping_model/warping_module/coarse_level/cnn_4/kernel/Initializer/random_uniform"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_4/kernel"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_4/kernel/read"
  op: "Identity"
  input: "warping_model/warping_module/coarse_level/cnn_4/kernel"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_4/kernel"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_4/dilation_rate"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 2
          }
        }
        tensor_content: "\001\000\000\000\001\000\000\000"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/coarse_level/cnn_4/Conv2D"
  op: "Conv2D"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/cond/Merge"
  input: "warping_model/warping_module/coarse_level/cnn_4/kernel/read"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "data_format"
    value {
      s: "NHWC"
    }
  }
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "use_cudnn_on_gpu"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/Tanh"
  op: "Tanh"
  input: "warping_model/warping_module/coarse_level/cnn_4/Conv2D"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/warping_module/resize_images/size"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 2
          }
        }
        tensor_content: "0\000\000\000@\000\000\000"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/resize_images/ResizeNearestNeighbor"
  op: "ResizeNearestNeighbor"
  input: "warping_model/warping_module/Tanh"
  input: "warping_model/warping_module/resize_images/size"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "align_corners"
    value {
      b: false
    }
  }
}
node {
  name: "warping_model/warping_module/average_pooling2d_1/AvgPool"
  op: "AvgPool"
  input: "warping_model/warping_module/resize_images/ResizeNearestNeighbor"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "data_format"
    value {
      s: "NHWC"
    }
  }
  attr {
    key: "ksize"
    value {
      list {
        i: 1
        i: 2
        i: 2
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_input/axis"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
        }
        int_val: 3
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_input"
  op: "ConcatV2"
  input: "warping_model/concat"
  input: "warping_model/warping_module/average_pooling2d_1/AvgPool"
  input: "warping_model/warping_module/fine_input/axis"
  attr {
    key: "N"
    value {
      i: 2
    }
  }
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "Tidx"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/cnn/kernel/Initializer/random_uniform/shape"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_0/cnn/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 4
          }
        }
        tensor_content: "\005\000\000\000\005\000\000\000/\000\000\000 \000\000\000"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/cnn/kernel/Initializer/random_uniform/min"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_0/cnn/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: -0.05511782690882683
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/cnn/kernel/Initializer/random_uniform/max"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_0/cnn/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 0.05511782690882683
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/cnn/kernel/Initializer/random_uniform/RandomUniform"
  op: "RandomUniform"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/cnn/kernel/Initializer/random_uniform/shape"
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_0/cnn/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "seed"
    value {
      i: 0
    }
  }
  attr {
    key: "seed2"
    value {
      i: 0
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/cnn/kernel/Initializer/random_uniform/sub"
  op: "Sub"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/cnn/kernel/Initializer/random_uniform/max"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/cnn/kernel/Initializer/random_uniform/min"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_0/cnn/kernel"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/cnn/kernel/Initializer/random_uniform/mul"
  op: "Mul"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/cnn/kernel/Initializer/random_uniform/RandomUniform"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/cnn/kernel/Initializer/random_uniform/sub"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_0/cnn/kernel"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/cnn/kernel/Initializer/random_uniform"
  op: "Add"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/cnn/kernel/Initializer/random_uniform/mul"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/cnn/kernel/Initializer/random_uniform/min"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_0/cnn/kernel"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/cnn/kernel"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_0/cnn/kernel"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 5
        }
        dim {
          size: 5
        }
        dim {
          size: 47
        }
        dim {
          size: 32
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/cnn/kernel/Assign"
  op: "Assign"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/cnn/kernel"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/cnn/kernel/Initializer/random_uniform"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_0/cnn/kernel"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/cnn/kernel/read"
  op: "Identity"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/cnn/kernel"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_0/cnn/kernel"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/cnn/dilation_rate"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 2
          }
        }
        tensor_content: "\001\000\000\000\001\000\000\000"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/cnn/Conv2D"
  op: "Conv2D"
  input: "warping_model/warping_module/fine_input"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/cnn/kernel/read"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "data_format"
    value {
      s: "NHWC"
    }
  }
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "use_cudnn_on_gpu"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/act"
  op: "Relu"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/cnn/Conv2D"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/gamma/Initializer/ones"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/gamma"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 32
          }
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/gamma"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/gamma"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 32
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/gamma/Assign"
  op: "Assign"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/gamma"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/gamma/Initializer/ones"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/gamma"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/gamma/read"
  op: "Identity"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/gamma"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/gamma"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/beta/Initializer/zeros"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/beta"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 32
          }
        }
        float_val: 0.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/beta"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/beta"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 32
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/beta/Assign"
  op: "Assign"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/beta"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/beta/Initializer/zeros"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/beta"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/beta/read"
  op: "Identity"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/beta"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/beta"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/moving_mean/Initializer/zeros"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 32
          }
        }
        float_val: 0.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/moving_mean"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 32
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/moving_mean/Assign"
  op: "Assign"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/moving_mean"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/moving_mean/Initializer/zeros"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/moving_mean/read"
  op: "Identity"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/moving_mean"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/moving_mean"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/moving_variance/Initializer/ones"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 32
          }
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/moving_variance"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 32
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/moving_variance/Assign"
  op: "Assign"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/moving_variance"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/moving_variance/Initializer/ones"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/moving_variance/read"
  op: "Identity"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/moving_variance"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/moving_variance"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond/Switch"
  op: "Switch"
  input: "inputs/phase_train"
  input: "inputs/phase_train"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond/switch_t"
  op: "Identity"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond/Switch:1"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond/switch_f"
  op: "Identity"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond/Switch"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond/pred_id"
  op: "Identity"
  input: "inputs/phase_train"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond/Const"
  op: "Const"
  input: "^warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond/switch_t"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
          }
        }
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond/Const_1"
  op: "Const"
  input: "^warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond/switch_t"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
          }
        }
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond/FusedBatchNorm"
  op: "FusedBatchNorm"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond/FusedBatchNorm/Switch:1"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond/FusedBatchNorm/Switch_1:1"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond/FusedBatchNorm/Switch_2:1"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond/Const"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond/Const_1"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "data_format"
    value {
      s: "NHWC"
    }
  }
  attr {
    key: "epsilon"
    value {
      f: 1.0009999641624745e-05
    }
  }
  attr {
    key: "is_training"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond/FusedBatchNorm/Switch"
  op: "Switch"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/act"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_0/act"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond/FusedBatchNorm/Switch_1"
  op: "Switch"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/gamma/read"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/gamma"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond/FusedBatchNorm/Switch_2"
  op: "Switch"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/beta/read"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/beta"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond/FusedBatchNorm_1"
  op: "FusedBatchNorm"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond/FusedBatchNorm_1/Switch"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond/FusedBatchNorm_1/Switch_1"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond/FusedBatchNorm_1/Switch_2"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond/FusedBatchNorm_1/Switch_3"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond/FusedBatchNorm_1/Switch_4"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "data_format"
    value {
      s: "NHWC"
    }
  }
  attr {
    key: "epsilon"
    value {
      f: 1.0009999641624745e-05
    }
  }
  attr {
    key: "is_training"
    value {
      b: false
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond/FusedBatchNorm_1/Switch"
  op: "Switch"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/act"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_0/act"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond/FusedBatchNorm_1/Switch_1"
  op: "Switch"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/gamma/read"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/gamma"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond/FusedBatchNorm_1/Switch_2"
  op: "Switch"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/beta/read"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/beta"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond/FusedBatchNorm_1/Switch_3"
  op: "Switch"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/moving_mean/read"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/moving_mean"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond/FusedBatchNorm_1/Switch_4"
  op: "Switch"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/moving_variance/read"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/moving_variance"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond/Merge"
  op: "Merge"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond/FusedBatchNorm_1"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond/FusedBatchNorm"
  attr {
    key: "N"
    value {
      i: 2
    }
  }
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond/Merge_1"
  op: "Merge"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond/FusedBatchNorm_1:1"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond/FusedBatchNorm:1"
  attr {
    key: "N"
    value {
      i: 2
    }
  }
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond/Merge_2"
  op: "Merge"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond/FusedBatchNorm_1:2"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond/FusedBatchNorm:2"
  attr {
    key: "N"
    value {
      i: 2
    }
  }
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond_1/Switch"
  op: "Switch"
  input: "inputs/phase_train"
  input: "inputs/phase_train"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond_1/switch_t"
  op: "Identity"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond_1/Switch:1"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond_1/switch_f"
  op: "Identity"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond_1/Switch"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond_1/pred_id"
  op: "Identity"
  input: "inputs/phase_train"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond_1/Const"
  op: "Const"
  input: "^warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond_1/switch_t"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 0.8999999761581421
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond_1/Const_1"
  op: "Const"
  input: "^warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond_1/switch_f"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond_1/Merge"
  op: "Merge"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond_1/Const_1"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond_1/Const"
  attr {
    key: "N"
    value {
      i: 2
    }
  }
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/AssignMovingAvg/sub/x"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/AssignMovingAvg/sub"
  op: "Sub"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/AssignMovingAvg/sub/x"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond_1/Merge"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/moving_mean"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/AssignMovingAvg/sub_1"
  op: "Sub"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/moving_mean/read"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond/Merge_1"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/moving_mean"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/AssignMovingAvg/mul"
  op: "Mul"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/AssignMovingAvg/sub_1"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/AssignMovingAvg/sub"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/moving_mean"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/AssignMovingAvg"
  op: "AssignSub"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/moving_mean"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/AssignMovingAvg/mul"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: false
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/AssignMovingAvg_1/sub/x"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/AssignMovingAvg_1/sub"
  op: "Sub"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/AssignMovingAvg_1/sub/x"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond_1/Merge"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/moving_variance"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/AssignMovingAvg_1/sub_1"
  op: "Sub"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/moving_variance/read"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond/Merge_2"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/moving_variance"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/AssignMovingAvg_1/mul"
  op: "Mul"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/AssignMovingAvg_1/sub_1"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/AssignMovingAvg_1/sub"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/moving_variance"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/AssignMovingAvg_1"
  op: "AssignSub"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/moving_variance"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/AssignMovingAvg_1/mul"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: false
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/cnn/kernel/Initializer/random_uniform/shape"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_1/cnn/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 4
          }
        }
        tensor_content: "\003\000\000\000\003\000\000\000 \000\000\000@\000\000\000"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/cnn/kernel/Initializer/random_uniform/min"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_1/cnn/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: -0.0833333358168602
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/cnn/kernel/Initializer/random_uniform/max"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_1/cnn/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 0.0833333358168602
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/cnn/kernel/Initializer/random_uniform/RandomUniform"
  op: "RandomUniform"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/cnn/kernel/Initializer/random_uniform/shape"
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_1/cnn/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "seed"
    value {
      i: 0
    }
  }
  attr {
    key: "seed2"
    value {
      i: 0
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/cnn/kernel/Initializer/random_uniform/sub"
  op: "Sub"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/cnn/kernel/Initializer/random_uniform/max"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/cnn/kernel/Initializer/random_uniform/min"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_1/cnn/kernel"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/cnn/kernel/Initializer/random_uniform/mul"
  op: "Mul"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/cnn/kernel/Initializer/random_uniform/RandomUniform"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/cnn/kernel/Initializer/random_uniform/sub"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_1/cnn/kernel"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/cnn/kernel/Initializer/random_uniform"
  op: "Add"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/cnn/kernel/Initializer/random_uniform/mul"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/cnn/kernel/Initializer/random_uniform/min"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_1/cnn/kernel"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/cnn/kernel"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_1/cnn/kernel"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 3
        }
        dim {
          size: 3
        }
        dim {
          size: 32
        }
        dim {
          size: 64
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/cnn/kernel/Assign"
  op: "Assign"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/cnn/kernel"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/cnn/kernel/Initializer/random_uniform"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_1/cnn/kernel"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/cnn/kernel/read"
  op: "Identity"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/cnn/kernel"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_1/cnn/kernel"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/cnn/dilation_rate"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 2
          }
        }
        tensor_content: "\001\000\000\000\001\000\000\000"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/cnn/Conv2D"
  op: "Conv2D"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond/Merge"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/cnn/kernel/read"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "data_format"
    value {
      s: "NHWC"
    }
  }
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "use_cudnn_on_gpu"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/act"
  op: "Relu"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/cnn/Conv2D"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/gamma/Initializer/ones"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/gamma"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 64
          }
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/gamma"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/gamma"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 64
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/gamma/Assign"
  op: "Assign"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/gamma"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/gamma/Initializer/ones"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/gamma"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/gamma/read"
  op: "Identity"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/gamma"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/gamma"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/beta/Initializer/zeros"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/beta"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 64
          }
        }
        float_val: 0.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/beta"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/beta"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 64
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/beta/Assign"
  op: "Assign"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/beta"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/beta/Initializer/zeros"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/beta"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/beta/read"
  op: "Identity"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/beta"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/beta"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/moving_mean/Initializer/zeros"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 64
          }
        }
        float_val: 0.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/moving_mean"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 64
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/moving_mean/Assign"
  op: "Assign"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/moving_mean"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/moving_mean/Initializer/zeros"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/moving_mean/read"
  op: "Identity"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/moving_mean"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/moving_mean"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/moving_variance/Initializer/ones"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 64
          }
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/moving_variance"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 64
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/moving_variance/Assign"
  op: "Assign"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/moving_variance"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/moving_variance/Initializer/ones"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/moving_variance/read"
  op: "Identity"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/moving_variance"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/moving_variance"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond/Switch"
  op: "Switch"
  input: "inputs/phase_train"
  input: "inputs/phase_train"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond/switch_t"
  op: "Identity"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond/Switch:1"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond/switch_f"
  op: "Identity"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond/Switch"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond/pred_id"
  op: "Identity"
  input: "inputs/phase_train"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond/Const"
  op: "Const"
  input: "^warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond/switch_t"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
          }
        }
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond/Const_1"
  op: "Const"
  input: "^warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond/switch_t"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
          }
        }
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond/FusedBatchNorm"
  op: "FusedBatchNorm"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond/FusedBatchNorm/Switch:1"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond/FusedBatchNorm/Switch_1:1"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond/FusedBatchNorm/Switch_2:1"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond/Const"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond/Const_1"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "data_format"
    value {
      s: "NHWC"
    }
  }
  attr {
    key: "epsilon"
    value {
      f: 1.0009999641624745e-05
    }
  }
  attr {
    key: "is_training"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond/FusedBatchNorm/Switch"
  op: "Switch"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/act"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_1/act"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond/FusedBatchNorm/Switch_1"
  op: "Switch"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/gamma/read"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/gamma"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond/FusedBatchNorm/Switch_2"
  op: "Switch"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/beta/read"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/beta"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond/FusedBatchNorm_1"
  op: "FusedBatchNorm"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond/FusedBatchNorm_1/Switch"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond/FusedBatchNorm_1/Switch_1"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond/FusedBatchNorm_1/Switch_2"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond/FusedBatchNorm_1/Switch_3"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond/FusedBatchNorm_1/Switch_4"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "data_format"
    value {
      s: "NHWC"
    }
  }
  attr {
    key: "epsilon"
    value {
      f: 1.0009999641624745e-05
    }
  }
  attr {
    key: "is_training"
    value {
      b: false
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond/FusedBatchNorm_1/Switch"
  op: "Switch"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/act"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_1/act"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond/FusedBatchNorm_1/Switch_1"
  op: "Switch"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/gamma/read"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/gamma"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond/FusedBatchNorm_1/Switch_2"
  op: "Switch"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/beta/read"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/beta"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond/FusedBatchNorm_1/Switch_3"
  op: "Switch"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/moving_mean/read"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/moving_mean"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond/FusedBatchNorm_1/Switch_4"
  op: "Switch"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/moving_variance/read"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/moving_variance"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond/Merge"
  op: "Merge"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond/FusedBatchNorm_1"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond/FusedBatchNorm"
  attr {
    key: "N"
    value {
      i: 2
    }
  }
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond/Merge_1"
  op: "Merge"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond/FusedBatchNorm_1:1"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond/FusedBatchNorm:1"
  attr {
    key: "N"
    value {
      i: 2
    }
  }
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond/Merge_2"
  op: "Merge"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond/FusedBatchNorm_1:2"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond/FusedBatchNorm:2"
  attr {
    key: "N"
    value {
      i: 2
    }
  }
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond_1/Switch"
  op: "Switch"
  input: "inputs/phase_train"
  input: "inputs/phase_train"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond_1/switch_t"
  op: "Identity"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond_1/Switch:1"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond_1/switch_f"
  op: "Identity"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond_1/Switch"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond_1/pred_id"
  op: "Identity"
  input: "inputs/phase_train"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond_1/Const"
  op: "Const"
  input: "^warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond_1/switch_t"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 0.8999999761581421
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond_1/Const_1"
  op: "Const"
  input: "^warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond_1/switch_f"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond_1/Merge"
  op: "Merge"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond_1/Const_1"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond_1/Const"
  attr {
    key: "N"
    value {
      i: 2
    }
  }
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/AssignMovingAvg/sub/x"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/AssignMovingAvg/sub"
  op: "Sub"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/AssignMovingAvg/sub/x"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond_1/Merge"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/moving_mean"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/AssignMovingAvg/sub_1"
  op: "Sub"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/moving_mean/read"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond/Merge_1"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/moving_mean"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/AssignMovingAvg/mul"
  op: "Mul"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/AssignMovingAvg/sub_1"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/AssignMovingAvg/sub"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/moving_mean"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/AssignMovingAvg"
  op: "AssignSub"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/moving_mean"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/AssignMovingAvg/mul"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: false
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/AssignMovingAvg_1/sub/x"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/AssignMovingAvg_1/sub"
  op: "Sub"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/AssignMovingAvg_1/sub/x"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond_1/Merge"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/moving_variance"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/AssignMovingAvg_1/sub_1"
  op: "Sub"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/moving_variance/read"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond/Merge_2"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/moving_variance"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/AssignMovingAvg_1/mul"
  op: "Mul"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/AssignMovingAvg_1/sub_1"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/AssignMovingAvg_1/sub"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/moving_variance"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/AssignMovingAvg_1"
  op: "AssignSub"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/moving_variance"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/AssignMovingAvg_1/mul"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: false
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/concat/axis"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
        }
        int_val: 3
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/concat"
  op: "ConcatV2"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond/Merge"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond/Merge"
  input: "warping_model/warping_module/fine_level/concat/axis"
  attr {
    key: "N"
    value {
      i: 2
    }
  }
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "Tidx"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/cnn/kernel/Initializer/random_uniform/shape"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_2/cnn/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 4
          }
        }
        tensor_content: "\003\000\000\000\003\000\000\000`\000\000\000 \000\000\000"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/cnn/kernel/Initializer/random_uniform/min"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_2/cnn/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: -0.07216878235340118
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/cnn/kernel/Initializer/random_uniform/max"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_2/cnn/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 0.07216878235340118
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/cnn/kernel/Initializer/random_uniform/RandomUniform"
  op: "RandomUniform"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/cnn/kernel/Initializer/random_uniform/shape"
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_2/cnn/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "seed"
    value {
      i: 0
    }
  }
  attr {
    key: "seed2"
    value {
      i: 0
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/cnn/kernel/Initializer/random_uniform/sub"
  op: "Sub"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/cnn/kernel/Initializer/random_uniform/max"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/cnn/kernel/Initializer/random_uniform/min"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_2/cnn/kernel"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/cnn/kernel/Initializer/random_uniform/mul"
  op: "Mul"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/cnn/kernel/Initializer/random_uniform/RandomUniform"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/cnn/kernel/Initializer/random_uniform/sub"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_2/cnn/kernel"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/cnn/kernel/Initializer/random_uniform"
  op: "Add"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/cnn/kernel/Initializer/random_uniform/mul"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/cnn/kernel/Initializer/random_uniform/min"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_2/cnn/kernel"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/cnn/kernel"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_2/cnn/kernel"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 3
        }
        dim {
          size: 3
        }
        dim {
          size: 96
        }
        dim {
          size: 32
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/cnn/kernel/Assign"
  op: "Assign"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/cnn/kernel"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/cnn/kernel/Initializer/random_uniform"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_2/cnn/kernel"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/cnn/kernel/read"
  op: "Identity"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/cnn/kernel"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_2/cnn/kernel"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/cnn/dilation_rate"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 2
          }
        }
        tensor_content: "\001\000\000\000\001\000\000\000"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/cnn/Conv2D"
  op: "Conv2D"
  input: "warping_model/warping_module/fine_level/concat"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/cnn/kernel/read"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "data_format"
    value {
      s: "NHWC"
    }
  }
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "use_cudnn_on_gpu"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/act"
  op: "Relu"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/cnn/Conv2D"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/gamma/Initializer/ones"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/gamma"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 32
          }
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/gamma"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/gamma"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 32
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/gamma/Assign"
  op: "Assign"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/gamma"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/gamma/Initializer/ones"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/gamma"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/gamma/read"
  op: "Identity"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/gamma"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/gamma"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/beta/Initializer/zeros"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/beta"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 32
          }
        }
        float_val: 0.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/beta"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/beta"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 32
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/beta/Assign"
  op: "Assign"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/beta"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/beta/Initializer/zeros"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/beta"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/beta/read"
  op: "Identity"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/beta"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/beta"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/moving_mean/Initializer/zeros"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 32
          }
        }
        float_val: 0.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/moving_mean"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 32
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/moving_mean/Assign"
  op: "Assign"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/moving_mean"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/moving_mean/Initializer/zeros"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/moving_mean/read"
  op: "Identity"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/moving_mean"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/moving_mean"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/moving_variance/Initializer/ones"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 32
          }
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/moving_variance"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 32
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/moving_variance/Assign"
  op: "Assign"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/moving_variance"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/moving_variance/Initializer/ones"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/moving_variance/read"
  op: "Identity"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/moving_variance"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/moving_variance"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond/Switch"
  op: "Switch"
  input: "inputs/phase_train"
  input: "inputs/phase_train"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond/switch_t"
  op: "Identity"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond/Switch:1"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond/switch_f"
  op: "Identity"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond/Switch"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond/pred_id"
  op: "Identity"
  input: "inputs/phase_train"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond/Const"
  op: "Const"
  input: "^warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond/switch_t"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
          }
        }
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond/Const_1"
  op: "Const"
  input: "^warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond/switch_t"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
          }
        }
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond/FusedBatchNorm"
  op: "FusedBatchNorm"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond/FusedBatchNorm/Switch:1"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond/FusedBatchNorm/Switch_1:1"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond/FusedBatchNorm/Switch_2:1"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond/Const"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond/Const_1"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "data_format"
    value {
      s: "NHWC"
    }
  }
  attr {
    key: "epsilon"
    value {
      f: 1.0009999641624745e-05
    }
  }
  attr {
    key: "is_training"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond/FusedBatchNorm/Switch"
  op: "Switch"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/act"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_2/act"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond/FusedBatchNorm/Switch_1"
  op: "Switch"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/gamma/read"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/gamma"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond/FusedBatchNorm/Switch_2"
  op: "Switch"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/beta/read"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/beta"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond/FusedBatchNorm_1"
  op: "FusedBatchNorm"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond/FusedBatchNorm_1/Switch"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond/FusedBatchNorm_1/Switch_1"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond/FusedBatchNorm_1/Switch_2"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond/FusedBatchNorm_1/Switch_3"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond/FusedBatchNorm_1/Switch_4"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "data_format"
    value {
      s: "NHWC"
    }
  }
  attr {
    key: "epsilon"
    value {
      f: 1.0009999641624745e-05
    }
  }
  attr {
    key: "is_training"
    value {
      b: false
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond/FusedBatchNorm_1/Switch"
  op: "Switch"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/act"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_2/act"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond/FusedBatchNorm_1/Switch_1"
  op: "Switch"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/gamma/read"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/gamma"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond/FusedBatchNorm_1/Switch_2"
  op: "Switch"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/beta/read"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/beta"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond/FusedBatchNorm_1/Switch_3"
  op: "Switch"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/moving_mean/read"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/moving_mean"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond/FusedBatchNorm_1/Switch_4"
  op: "Switch"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/moving_variance/read"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/moving_variance"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond/Merge"
  op: "Merge"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond/FusedBatchNorm_1"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond/FusedBatchNorm"
  attr {
    key: "N"
    value {
      i: 2
    }
  }
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond/Merge_1"
  op: "Merge"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond/FusedBatchNorm_1:1"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond/FusedBatchNorm:1"
  attr {
    key: "N"
    value {
      i: 2
    }
  }
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond/Merge_2"
  op: "Merge"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond/FusedBatchNorm_1:2"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond/FusedBatchNorm:2"
  attr {
    key: "N"
    value {
      i: 2
    }
  }
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond_1/Switch"
  op: "Switch"
  input: "inputs/phase_train"
  input: "inputs/phase_train"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond_1/switch_t"
  op: "Identity"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond_1/Switch:1"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond_1/switch_f"
  op: "Identity"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond_1/Switch"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond_1/pred_id"
  op: "Identity"
  input: "inputs/phase_train"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond_1/Const"
  op: "Const"
  input: "^warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond_1/switch_t"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 0.8999999761581421
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond_1/Const_1"
  op: "Const"
  input: "^warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond_1/switch_f"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond_1/Merge"
  op: "Merge"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond_1/Const_1"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond_1/Const"
  attr {
    key: "N"
    value {
      i: 2
    }
  }
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/AssignMovingAvg/sub/x"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/AssignMovingAvg/sub"
  op: "Sub"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/AssignMovingAvg/sub/x"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond_1/Merge"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/moving_mean"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/AssignMovingAvg/sub_1"
  op: "Sub"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/moving_mean/read"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond/Merge_1"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/moving_mean"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/AssignMovingAvg/mul"
  op: "Mul"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/AssignMovingAvg/sub_1"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/AssignMovingAvg/sub"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/moving_mean"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/AssignMovingAvg"
  op: "AssignSub"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/moving_mean"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/AssignMovingAvg/mul"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: false
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/AssignMovingAvg_1/sub/x"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/AssignMovingAvg_1/sub"
  op: "Sub"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/AssignMovingAvg_1/sub/x"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond_1/Merge"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/moving_variance"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/AssignMovingAvg_1/sub_1"
  op: "Sub"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/moving_variance/read"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond/Merge_2"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/moving_variance"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/AssignMovingAvg_1/mul"
  op: "Mul"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/AssignMovingAvg_1/sub_1"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/AssignMovingAvg_1/sub"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/moving_variance"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/AssignMovingAvg_1"
  op: "AssignSub"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/moving_variance"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/AssignMovingAvg_1/mul"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: false
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/concat_1/axis"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
        }
        int_val: 3
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/concat_1"
  op: "ConcatV2"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/cond/Merge"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/cond/Merge"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/cond/Merge"
  input: "warping_model/warping_module/fine_level/concat_1/axis"
  attr {
    key: "N"
    value {
      i: 3
    }
  }
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "Tidx"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/cnn/kernel/Initializer/random_uniform/shape"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_3/cnn/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 4
          }
        }
        tensor_content: "\003\000\000\000\003\000\000\000\200\000\000\000\020\000\000\000"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/cnn/kernel/Initializer/random_uniform/min"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_3/cnn/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: -0.06804138422012329
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/cnn/kernel/Initializer/random_uniform/max"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_3/cnn/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 0.06804138422012329
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/cnn/kernel/Initializer/random_uniform/RandomUniform"
  op: "RandomUniform"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/cnn/kernel/Initializer/random_uniform/shape"
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_3/cnn/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "seed"
    value {
      i: 0
    }
  }
  attr {
    key: "seed2"
    value {
      i: 0
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/cnn/kernel/Initializer/random_uniform/sub"
  op: "Sub"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/cnn/kernel/Initializer/random_uniform/max"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/cnn/kernel/Initializer/random_uniform/min"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_3/cnn/kernel"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/cnn/kernel/Initializer/random_uniform/mul"
  op: "Mul"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/cnn/kernel/Initializer/random_uniform/RandomUniform"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/cnn/kernel/Initializer/random_uniform/sub"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_3/cnn/kernel"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/cnn/kernel/Initializer/random_uniform"
  op: "Add"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/cnn/kernel/Initializer/random_uniform/mul"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/cnn/kernel/Initializer/random_uniform/min"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_3/cnn/kernel"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/cnn/kernel"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_3/cnn/kernel"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 3
        }
        dim {
          size: 3
        }
        dim {
          size: 128
        }
        dim {
          size: 16
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/cnn/kernel/Assign"
  op: "Assign"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/cnn/kernel"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/cnn/kernel/Initializer/random_uniform"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_3/cnn/kernel"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/cnn/kernel/read"
  op: "Identity"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/cnn/kernel"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_3/cnn/kernel"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/cnn/dilation_rate"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 2
          }
        }
        tensor_content: "\001\000\000\000\001\000\000\000"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/cnn/Conv2D"
  op: "Conv2D"
  input: "warping_model/warping_module/fine_level/concat_1"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/cnn/kernel/read"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "data_format"
    value {
      s: "NHWC"
    }
  }
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "use_cudnn_on_gpu"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/act"
  op: "Relu"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/cnn/Conv2D"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/gamma/Initializer/ones"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/gamma"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 16
          }
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/gamma"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/gamma"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 16
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/gamma/Assign"
  op: "Assign"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/gamma"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/gamma/Initializer/ones"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/gamma"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/gamma/read"
  op: "Identity"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/gamma"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/gamma"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/beta/Initializer/zeros"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/beta"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 16
          }
        }
        float_val: 0.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/beta"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/beta"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 16
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/beta/Assign"
  op: "Assign"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/beta"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/beta/Initializer/zeros"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/beta"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/beta/read"
  op: "Identity"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/beta"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/beta"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/moving_mean/Initializer/zeros"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 16
          }
        }
        float_val: 0.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/moving_mean"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 16
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/moving_mean/Assign"
  op: "Assign"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/moving_mean"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/moving_mean/Initializer/zeros"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/moving_mean/read"
  op: "Identity"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/moving_mean"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/moving_mean"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/moving_variance/Initializer/ones"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 16
          }
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/moving_variance"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 16
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/moving_variance/Assign"
  op: "Assign"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/moving_variance"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/moving_variance/Initializer/ones"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/moving_variance/read"
  op: "Identity"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/moving_variance"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/moving_variance"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond/Switch"
  op: "Switch"
  input: "inputs/phase_train"
  input: "inputs/phase_train"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond/switch_t"
  op: "Identity"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond/Switch:1"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond/switch_f"
  op: "Identity"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond/Switch"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond/pred_id"
  op: "Identity"
  input: "inputs/phase_train"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond/Const"
  op: "Const"
  input: "^warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond/switch_t"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
          }
        }
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond/Const_1"
  op: "Const"
  input: "^warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond/switch_t"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
          }
        }
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond/FusedBatchNorm"
  op: "FusedBatchNorm"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond/FusedBatchNorm/Switch:1"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond/FusedBatchNorm/Switch_1:1"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond/FusedBatchNorm/Switch_2:1"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond/Const"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond/Const_1"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "data_format"
    value {
      s: "NHWC"
    }
  }
  attr {
    key: "epsilon"
    value {
      f: 1.0009999641624745e-05
    }
  }
  attr {
    key: "is_training"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond/FusedBatchNorm/Switch"
  op: "Switch"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/act"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_3/act"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond/FusedBatchNorm/Switch_1"
  op: "Switch"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/gamma/read"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/gamma"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond/FusedBatchNorm/Switch_2"
  op: "Switch"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/beta/read"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/beta"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond/FusedBatchNorm_1"
  op: "FusedBatchNorm"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond/FusedBatchNorm_1/Switch"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond/FusedBatchNorm_1/Switch_1"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond/FusedBatchNorm_1/Switch_2"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond/FusedBatchNorm_1/Switch_3"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond/FusedBatchNorm_1/Switch_4"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "data_format"
    value {
      s: "NHWC"
    }
  }
  attr {
    key: "epsilon"
    value {
      f: 1.0009999641624745e-05
    }
  }
  attr {
    key: "is_training"
    value {
      b: false
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond/FusedBatchNorm_1/Switch"
  op: "Switch"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/act"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_3/act"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond/FusedBatchNorm_1/Switch_1"
  op: "Switch"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/gamma/read"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/gamma"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond/FusedBatchNorm_1/Switch_2"
  op: "Switch"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/beta/read"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/beta"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond/FusedBatchNorm_1/Switch_3"
  op: "Switch"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/moving_mean/read"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/moving_mean"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond/FusedBatchNorm_1/Switch_4"
  op: "Switch"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/moving_variance/read"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/moving_variance"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond/Merge"
  op: "Merge"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond/FusedBatchNorm_1"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond/FusedBatchNorm"
  attr {
    key: "N"
    value {
      i: 2
    }
  }
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond/Merge_1"
  op: "Merge"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond/FusedBatchNorm_1:1"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond/FusedBatchNorm:1"
  attr {
    key: "N"
    value {
      i: 2
    }
  }
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond/Merge_2"
  op: "Merge"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond/FusedBatchNorm_1:2"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond/FusedBatchNorm:2"
  attr {
    key: "N"
    value {
      i: 2
    }
  }
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond_1/Switch"
  op: "Switch"
  input: "inputs/phase_train"
  input: "inputs/phase_train"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond_1/switch_t"
  op: "Identity"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond_1/Switch:1"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond_1/switch_f"
  op: "Identity"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond_1/Switch"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond_1/pred_id"
  op: "Identity"
  input: "inputs/phase_train"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond_1/Const"
  op: "Const"
  input: "^warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond_1/switch_t"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 0.8999999761581421
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond_1/Const_1"
  op: "Const"
  input: "^warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond_1/switch_f"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond_1/Merge"
  op: "Merge"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond_1/Const_1"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond_1/Const"
  attr {
    key: "N"
    value {
      i: 2
    }
  }
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/AssignMovingAvg/sub/x"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/AssignMovingAvg/sub"
  op: "Sub"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/AssignMovingAvg/sub/x"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond_1/Merge"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/moving_mean"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/AssignMovingAvg/sub_1"
  op: "Sub"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/moving_mean/read"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond/Merge_1"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/moving_mean"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/AssignMovingAvg/mul"
  op: "Mul"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/AssignMovingAvg/sub_1"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/AssignMovingAvg/sub"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/moving_mean"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/AssignMovingAvg"
  op: "AssignSub"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/moving_mean"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/AssignMovingAvg/mul"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: false
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/AssignMovingAvg_1/sub/x"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/AssignMovingAvg_1/sub"
  op: "Sub"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/AssignMovingAvg_1/sub/x"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond_1/Merge"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/moving_variance"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/AssignMovingAvg_1/sub_1"
  op: "Sub"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/moving_variance/read"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond/Merge_2"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/moving_variance"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/AssignMovingAvg_1/mul"
  op: "Mul"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/AssignMovingAvg_1/sub_1"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/AssignMovingAvg_1/sub"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/moving_variance"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/AssignMovingAvg_1"
  op: "AssignSub"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/moving_variance"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/AssignMovingAvg_1/mul"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: false
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_4/kernel/Initializer/random_uniform/shape"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_4/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 4
          }
        }
        tensor_content: "\001\000\000\000\001\000\000\000\020\000\000\000\004\000\000\000"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_4/kernel/Initializer/random_uniform/min"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_4/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: -0.547722578048706
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_4/kernel/Initializer/random_uniform/max"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_4/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 0.547722578048706
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_4/kernel/Initializer/random_uniform/RandomUniform"
  op: "RandomUniform"
  input: "warping_model/warping_module/fine_level/cnn_4/kernel/Initializer/random_uniform/shape"
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_4/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "seed"
    value {
      i: 0
    }
  }
  attr {
    key: "seed2"
    value {
      i: 0
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_4/kernel/Initializer/random_uniform/sub"
  op: "Sub"
  input: "warping_model/warping_module/fine_level/cnn_4/kernel/Initializer/random_uniform/max"
  input: "warping_model/warping_module/fine_level/cnn_4/kernel/Initializer/random_uniform/min"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_4/kernel"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_4/kernel/Initializer/random_uniform/mul"
  op: "Mul"
  input: "warping_model/warping_module/fine_level/cnn_4/kernel/Initializer/random_uniform/RandomUniform"
  input: "warping_model/warping_module/fine_level/cnn_4/kernel/Initializer/random_uniform/sub"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_4/kernel"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_4/kernel/Initializer/random_uniform"
  op: "Add"
  input: "warping_model/warping_module/fine_level/cnn_4/kernel/Initializer/random_uniform/mul"
  input: "warping_model/warping_module/fine_level/cnn_4/kernel/Initializer/random_uniform/min"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_4/kernel"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_4/kernel"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_4/kernel"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 1
        }
        dim {
          size: 1
        }
        dim {
          size: 16
        }
        dim {
          size: 4
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_4/kernel/Assign"
  op: "Assign"
  input: "warping_model/warping_module/fine_level/cnn_4/kernel"
  input: "warping_model/warping_module/fine_level/cnn_4/kernel/Initializer/random_uniform"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_4/kernel"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_4/kernel/read"
  op: "Identity"
  input: "warping_model/warping_module/fine_level/cnn_4/kernel"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_4/kernel"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_4/dilation_rate"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 2
          }
        }
        tensor_content: "\001\000\000\000\001\000\000\000"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/fine_level/cnn_4/Conv2D"
  op: "Conv2D"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/cond/Merge"
  input: "warping_model/warping_module/fine_level/cnn_4/kernel/read"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "data_format"
    value {
      s: "NHWC"
    }
  }
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "use_cudnn_on_gpu"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/warping_module/Const"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 2
          }
        }
        tensor_content: "\002\000\000\000\002\000\000\000"
      }
    }
  }
}
node {
  name: "warping_model/warping_module/split/split_dim"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
        }
        int_val: 3
      }
    }
  }
}
node {
  name: "warping_model/warping_module/split"
  op: "SplitV"
  input: "warping_model/warping_module/fine_level/cnn_4/Conv2D"
  input: "warping_model/warping_module/Const"
  input: "warping_model/warping_module/split/split_dim"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "Tlen"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "num_split"
    value {
      i: 2
    }
  }
}
node {
  name: "warping_model/Tanh"
  op: "Tanh"
  input: "warping_model/warping_module/split"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/apply_transformation/Shape"
  op: "Shape"
  input: "inputs/input_img"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "out_type"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/strided_slice/stack"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 1
          }
        }
        int_val: 0
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/strided_slice/stack_1"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 1
          }
        }
        int_val: 1
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/strided_slice/stack_2"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 1
          }
        }
        int_val: 1
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/strided_slice"
  op: "StridedSlice"
  input: "warping_model/apply_transformation/Shape"
  input: "warping_model/apply_transformation/strided_slice/stack"
  input: "warping_model/apply_transformation/strided_slice/stack_1"
  input: "warping_model/apply_transformation/strided_slice/stack_2"
  attr {
    key: "Index"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "begin_mask"
    value {
      i: 0
    }
  }
  attr {
    key: "ellipsis_mask"
    value {
      i: 0
    }
  }
  attr {
    key: "end_mask"
    value {
      i: 0
    }
  }
  attr {
    key: "new_axis_mask"
    value {
      i: 0
    }
  }
  attr {
    key: "shrink_axis_mask"
    value {
      i: 1
    }
  }
}
node {
  name: "warping_model/apply_transformation/Shape_1"
  op: "Shape"
  input: "inputs/input_img"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "out_type"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/strided_slice_1/stack"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 1
          }
        }
        int_val: 1
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/strided_slice_1/stack_1"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 1
          }
        }
        int_val: 2
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/strided_slice_1/stack_2"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 1
          }
        }
        int_val: 1
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/strided_slice_1"
  op: "StridedSlice"
  input: "warping_model/apply_transformation/Shape_1"
  input: "warping_model/apply_transformation/strided_slice_1/stack"
  input: "warping_model/apply_transformation/strided_slice_1/stack_1"
  input: "warping_model/apply_transformation/strided_slice_1/stack_2"
  attr {
    key: "Index"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "begin_mask"
    value {
      i: 0
    }
  }
  attr {
    key: "ellipsis_mask"
    value {
      i: 0
    }
  }
  attr {
    key: "end_mask"
    value {
      i: 0
    }
  }
  attr {
    key: "new_axis_mask"
    value {
      i: 0
    }
  }
  attr {
    key: "shrink_axis_mask"
    value {
      i: 1
    }
  }
}
node {
  name: "warping_model/apply_transformation/Shape_2"
  op: "Shape"
  input: "inputs/input_img"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "out_type"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/strided_slice_2/stack"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 1
          }
        }
        int_val: 2
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/strided_slice_2/stack_1"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 1
          }
        }
        int_val: 3
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/strided_slice_2/stack_2"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 1
          }
        }
        int_val: 1
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/strided_slice_2"
  op: "StridedSlice"
  input: "warping_model/apply_transformation/Shape_2"
  input: "warping_model/apply_transformation/strided_slice_2/stack"
  input: "warping_model/apply_transformation/strided_slice_2/stack_1"
  input: "warping_model/apply_transformation/strided_slice_2/stack_2"
  attr {
    key: "Index"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "begin_mask"
    value {
      i: 0
    }
  }
  attr {
    key: "ellipsis_mask"
    value {
      i: 0
    }
  }
  attr {
    key: "end_mask"
    value {
      i: 0
    }
  }
  attr {
    key: "new_axis_mask"
    value {
      i: 0
    }
  }
  attr {
    key: "shrink_axis_mask"
    value {
      i: 1
    }
  }
}
node {
  name: "warping_model/apply_transformation/Shape_3"
  op: "Shape"
  input: "warping_model/Tanh"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "out_type"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/strided_slice_3/stack"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 1
          }
        }
        int_val: 3
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/strided_slice_3/stack_1"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 1
          }
        }
        int_val: 4
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/strided_slice_3/stack_2"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 1
          }
        }
        int_val: 1
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/strided_slice_3"
  op: "StridedSlice"
  input: "warping_model/apply_transformation/Shape_3"
  input: "warping_model/apply_transformation/strided_slice_3/stack"
  input: "warping_model/apply_transformation/strided_slice_3/stack_1"
  input: "warping_model/apply_transformation/strided_slice_3/stack_2"
  attr {
    key: "Index"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "begin_mask"
    value {
      i: 0
    }
  }
  attr {
    key: "ellipsis_mask"
    value {
      i: 0
    }
  }
  attr {
    key: "end_mask"
    value {
      i: 0
    }
  }
  attr {
    key: "new_axis_mask"
    value {
      i: 0
    }
  }
  attr {
    key: "shrink_axis_mask"
    value {
      i: 1
    }
  }
}
node {
  name: "warping_model/apply_transformation/transpose/perm"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 4
          }
        }
        tensor_content: "\000\000\000\000\003\000\000\000\001\000\000\000\002\000\000\000"
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/transpose"
  op: "Transpose"
  input: "warping_model/Tanh"
  input: "warping_model/apply_transformation/transpose/perm"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "Tperm"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/mul"
  op: "Mul"
  input: "warping_model/apply_transformation/strided_slice_1"
  input: "warping_model/apply_transformation/strided_slice_2"
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/Reshape/shape"
  op: "Pack"
  input: "warping_model/apply_transformation/strided_slice"
  input: "warping_model/apply_transformation/strided_slice_3"
  input: "warping_model/apply_transformation/mul"
  attr {
    key: "N"
    value {
      i: 3
    }
  }
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "axis"
    value {
      i: 0
    }
  }
}
node {
  name: "warping_model/apply_transformation/Reshape"
  op: "Reshape"
  input: "warping_model/apply_transformation/transpose"
  input: "warping_model/apply_transformation/Reshape/shape"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "Tshape"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/meshgrid/LinSpace/start"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: -1.0
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/meshgrid/LinSpace/stop"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/meshgrid/LinSpace"
  op: "LinSpace"
  input: "warping_model/apply_transformation/meshgrid/LinSpace/start"
  input: "warping_model/apply_transformation/meshgrid/LinSpace/stop"
  input: "warping_model/apply_transformation/strided_slice_1"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "Tidx"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/meshgrid/LinSpace_1/start"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: -1.0
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/meshgrid/LinSpace_1/stop"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/meshgrid/LinSpace_1"
  op: "LinSpace"
  input: "warping_model/apply_transformation/meshgrid/LinSpace_1/start"
  input: "warping_model/apply_transformation/meshgrid/LinSpace_1/stop"
  input: "warping_model/apply_transformation/strided_slice_2"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "Tidx"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/meshgrid/meshgrid/Reshape/shape"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 2
          }
        }
        tensor_content: "\377\377\377\377\001\000\000\000"
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/meshgrid/meshgrid/Reshape"
  op: "Reshape"
  input: "warping_model/apply_transformation/meshgrid/LinSpace_1"
  input: "warping_model/apply_transformation/meshgrid/meshgrid/Reshape/shape"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "Tshape"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/meshgrid/meshgrid/Reshape_1/shape"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 2
          }
        }
        tensor_content: "\001\000\000\000\377\377\377\377"
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/meshgrid/meshgrid/Reshape_1"
  op: "Reshape"
  input: "warping_model/apply_transformation/meshgrid/LinSpace"
  input: "warping_model/apply_transformation/meshgrid/meshgrid/Reshape_1/shape"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "Tshape"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/meshgrid/meshgrid/Size"
  op: "Size"
  input: "warping_model/apply_transformation/meshgrid/LinSpace_1"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "out_type"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/meshgrid/meshgrid/Size_1"
  op: "Size"
  input: "warping_model/apply_transformation/meshgrid/LinSpace"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "out_type"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/meshgrid/meshgrid/Reshape_2/shape"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 2
          }
        }
        tensor_content: "\001\000\000\000\377\377\377\377"
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/meshgrid/meshgrid/Reshape_2"
  op: "Reshape"
  input: "warping_model/apply_transformation/meshgrid/meshgrid/Reshape"
  input: "warping_model/apply_transformation/meshgrid/meshgrid/Reshape_2/shape"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "Tshape"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/meshgrid/meshgrid/Reshape_3/shape"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 2
          }
        }
        tensor_content: "\377\377\377\377\001\000\000\000"
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/meshgrid/meshgrid/Reshape_3"
  op: "Reshape"
  input: "warping_model/apply_transformation/meshgrid/meshgrid/Reshape_1"
  input: "warping_model/apply_transformation/meshgrid/meshgrid/Reshape_3/shape"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "Tshape"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/meshgrid/meshgrid/ones/mul"
  op: "Mul"
  input: "warping_model/apply_transformation/meshgrid/meshgrid/Size_1"
  input: "warping_model/apply_transformation/meshgrid/meshgrid/Size"
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/meshgrid/meshgrid/ones/Less/y"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
        }
        int_val: 1000
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/meshgrid/meshgrid/ones/Less"
  op: "Less"
  input: "warping_model/apply_transformation/meshgrid/meshgrid/ones/mul"
  input: "warping_model/apply_transformation/meshgrid/meshgrid/ones/Less/y"
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/meshgrid/meshgrid/ones/packed"
  op: "Pack"
  input: "warping_model/apply_transformation/meshgrid/meshgrid/Size_1"
  input: "warping_model/apply_transformation/meshgrid/meshgrid/Size"
  attr {
    key: "N"
    value {
      i: 2
    }
  }
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "axis"
    value {
      i: 0
    }
  }
}
node {
  name: "warping_model/apply_transformation/meshgrid/meshgrid/ones/Const"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/meshgrid/meshgrid/ones"
  op: "Fill"
  input: "warping_model/apply_transformation/meshgrid/meshgrid/ones/packed"
  input: "warping_model/apply_transformation/meshgrid/meshgrid/ones/Const"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "index_type"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/meshgrid/meshgrid/mul"
  op: "Mul"
  input: "warping_model/apply_transformation/meshgrid/meshgrid/Reshape_2"
  input: "warping_model/apply_transformation/meshgrid/meshgrid/ones"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/apply_transformation/meshgrid/meshgrid/mul_1"
  op: "Mul"
  input: "warping_model/apply_transformation/meshgrid/meshgrid/Reshape_3"
  input: "warping_model/apply_transformation/meshgrid/meshgrid/ones"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/apply_transformation/meshgrid/Reshape/shape"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 1
          }
        }
        int_val: -1
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/meshgrid/Reshape"
  op: "Reshape"
  input: "warping_model/apply_transformation/meshgrid/meshgrid/mul_1"
  input: "warping_model/apply_transformation/meshgrid/Reshape/shape"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "Tshape"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/meshgrid/ExpandDims/dim"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
        }
        int_val: 0
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/meshgrid/ExpandDims"
  op: "ExpandDims"
  input: "warping_model/apply_transformation/meshgrid/Reshape"
  input: "warping_model/apply_transformation/meshgrid/ExpandDims/dim"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "Tdim"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/meshgrid/Reshape_1/shape"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 1
          }
        }
        int_val: -1
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/meshgrid/Reshape_1"
  op: "Reshape"
  input: "warping_model/apply_transformation/meshgrid/meshgrid/mul"
  input: "warping_model/apply_transformation/meshgrid/Reshape_1/shape"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "Tshape"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/meshgrid/ExpandDims_1/dim"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
        }
        int_val: 0
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/meshgrid/ExpandDims_1"
  op: "ExpandDims"
  input: "warping_model/apply_transformation/meshgrid/Reshape_1"
  input: "warping_model/apply_transformation/meshgrid/ExpandDims_1/dim"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "Tdim"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/meshgrid/concat/axis"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
        }
        int_val: 0
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/meshgrid/concat"
  op: "ConcatV2"
  input: "warping_model/apply_transformation/meshgrid/ExpandDims_1"
  input: "warping_model/apply_transformation/meshgrid/ExpandDims"
  input: "warping_model/apply_transformation/meshgrid/concat/axis"
  attr {
    key: "N"
    value {
      i: 2
    }
  }
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "Tidx"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/Add"
  op: "Add"
  input: "warping_model/apply_transformation/Reshape"
  input: "warping_model/apply_transformation/meshgrid/concat"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/apply_transformation/Slice/begin"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 3
          }
        }
        tensor_content: "\000\000\000\000\000\000\000\000\000\000\000\000"
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/Slice/size"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 3
          }
        }
        tensor_content: "\377\377\377\377\001\000\000\000\377\377\377\377"
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/Slice"
  op: "Slice"
  input: "warping_model/apply_transformation/Add"
  input: "warping_model/apply_transformation/Slice/begin"
  input: "warping_model/apply_transformation/Slice/size"
  attr {
    key: "Index"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/apply_transformation/Slice_1/begin"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 3
          }
        }
        tensor_content: "\000\000\000\000\001\000\000\000\000\000\000\000"
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/Slice_1/size"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 3
          }
        }
        tensor_content: "\377\377\377\377\001\000\000\000\377\377\377\377"
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/Slice_1"
  op: "Slice"
  input: "warping_model/apply_transformation/Add"
  input: "warping_model/apply_transformation/Slice_1/begin"
  input: "warping_model/apply_transformation/Slice_1/size"
  attr {
    key: "Index"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/apply_transformation/Reshape_1/shape"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 1
          }
        }
        int_val: -1
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/Reshape_1"
  op: "Reshape"
  input: "warping_model/apply_transformation/Slice"
  input: "warping_model/apply_transformation/Reshape_1/shape"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "Tshape"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/Reshape_2/shape"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 1
          }
        }
        int_val: -1
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/Reshape_2"
  op: "Reshape"
  input: "warping_model/apply_transformation/Slice_1"
  input: "warping_model/apply_transformation/Reshape_2/shape"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "Tshape"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/Shape"
  op: "Shape"
  input: "inputs/input_img"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "out_type"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/strided_slice/stack"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 1
          }
        }
        int_val: 0
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/strided_slice/stack_1"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 1
          }
        }
        int_val: 1
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/strided_slice/stack_2"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 1
          }
        }
        int_val: 1
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/strided_slice"
  op: "StridedSlice"
  input: "warping_model/apply_transformation/interpolate/Shape"
  input: "warping_model/apply_transformation/interpolate/strided_slice/stack"
  input: "warping_model/apply_transformation/interpolate/strided_slice/stack_1"
  input: "warping_model/apply_transformation/interpolate/strided_slice/stack_2"
  attr {
    key: "Index"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "begin_mask"
    value {
      i: 0
    }
  }
  attr {
    key: "ellipsis_mask"
    value {
      i: 0
    }
  }
  attr {
    key: "end_mask"
    value {
      i: 0
    }
  }
  attr {
    key: "new_axis_mask"
    value {
      i: 0
    }
  }
  attr {
    key: "shrink_axis_mask"
    value {
      i: 1
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/Shape_1"
  op: "Shape"
  input: "inputs/input_img"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "out_type"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/strided_slice_1/stack"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 1
          }
        }
        int_val: 1
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/strided_slice_1/stack_1"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 1
          }
        }
        int_val: 2
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/strided_slice_1/stack_2"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 1
          }
        }
        int_val: 1
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/strided_slice_1"
  op: "StridedSlice"
  input: "warping_model/apply_transformation/interpolate/Shape_1"
  input: "warping_model/apply_transformation/interpolate/strided_slice_1/stack"
  input: "warping_model/apply_transformation/interpolate/strided_slice_1/stack_1"
  input: "warping_model/apply_transformation/interpolate/strided_slice_1/stack_2"
  attr {
    key: "Index"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "begin_mask"
    value {
      i: 0
    }
  }
  attr {
    key: "ellipsis_mask"
    value {
      i: 0
    }
  }
  attr {
    key: "end_mask"
    value {
      i: 0
    }
  }
  attr {
    key: "new_axis_mask"
    value {
      i: 0
    }
  }
  attr {
    key: "shrink_axis_mask"
    value {
      i: 1
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/Shape_2"
  op: "Shape"
  input: "inputs/input_img"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "out_type"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/strided_slice_2/stack"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 1
          }
        }
        int_val: 2
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/strided_slice_2/stack_1"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 1
          }
        }
        int_val: 3
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/strided_slice_2/stack_2"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 1
          }
        }
        int_val: 1
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/strided_slice_2"
  op: "StridedSlice"
  input: "warping_model/apply_transformation/interpolate/Shape_2"
  input: "warping_model/apply_transformation/interpolate/strided_slice_2/stack"
  input: "warping_model/apply_transformation/interpolate/strided_slice_2/stack_1"
  input: "warping_model/apply_transformation/interpolate/strided_slice_2/stack_2"
  attr {
    key: "Index"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "begin_mask"
    value {
      i: 0
    }
  }
  attr {
    key: "ellipsis_mask"
    value {
      i: 0
    }
  }
  attr {
    key: "end_mask"
    value {
      i: 0
    }
  }
  attr {
    key: "new_axis_mask"
    value {
      i: 0
    }
  }
  attr {
    key: "shrink_axis_mask"
    value {
      i: 1
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/Shape_3"
  op: "Shape"
  input: "inputs/input_img"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "out_type"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/strided_slice_3/stack"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 1
          }
        }
        int_val: 3
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/strided_slice_3/stack_1"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 1
          }
        }
        int_val: 4
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/strided_slice_3/stack_2"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 1
          }
        }
        int_val: 1
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/strided_slice_3"
  op: "StridedSlice"
  input: "warping_model/apply_transformation/interpolate/Shape_3"
  input: "warping_model/apply_transformation/interpolate/strided_slice_3/stack"
  input: "warping_model/apply_transformation/interpolate/strided_slice_3/stack_1"
  input: "warping_model/apply_transformation/interpolate/strided_slice_3/stack_2"
  attr {
    key: "Index"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "begin_mask"
    value {
      i: 0
    }
  }
  attr {
    key: "ellipsis_mask"
    value {
      i: 0
    }
  }
  attr {
    key: "end_mask"
    value {
      i: 0
    }
  }
  attr {
    key: "new_axis_mask"
    value {
      i: 0
    }
  }
  attr {
    key: "shrink_axis_mask"
    value {
      i: 1
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/Cast"
  op: "Cast"
  input: "warping_model/apply_transformation/interpolate/strided_slice_1"
  attr {
    key: "DstT"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "SrcT"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/Cast_1"
  op: "Cast"
  input: "warping_model/apply_transformation/interpolate/strided_slice_2"
  attr {
    key: "DstT"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "SrcT"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/add/y"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/add"
  op: "Add"
  input: "warping_model/apply_transformation/Reshape_1"
  input: "warping_model/apply_transformation/interpolate/add/y"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/mul/x"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 0.5
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/mul"
  op: "Mul"
  input: "warping_model/apply_transformation/interpolate/mul/x"
  input: "warping_model/apply_transformation/interpolate/add"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/mul_1"
  op: "Mul"
  input: "warping_model/apply_transformation/interpolate/mul"
  input: "warping_model/apply_transformation/interpolate/Cast_1"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/add_1/y"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/add_1"
  op: "Add"
  input: "warping_model/apply_transformation/Reshape_2"
  input: "warping_model/apply_transformation/interpolate/add_1/y"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/mul_2/x"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 0.5
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/mul_2"
  op: "Mul"
  input: "warping_model/apply_transformation/interpolate/mul_2/x"
  input: "warping_model/apply_transformation/interpolate/add_1"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/mul_3"
  op: "Mul"
  input: "warping_model/apply_transformation/interpolate/mul_2"
  input: "warping_model/apply_transformation/interpolate/Cast"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/Floor"
  op: "Floor"
  input: "warping_model/apply_transformation/interpolate/mul_1"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/Cast_2"
  op: "Cast"
  input: "warping_model/apply_transformation/interpolate/Floor"
  attr {
    key: "DstT"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "SrcT"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/add_2/y"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
        }
        int_val: 1
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/add_2"
  op: "Add"
  input: "warping_model/apply_transformation/interpolate/Cast_2"
  input: "warping_model/apply_transformation/interpolate/add_2/y"
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/Floor_1"
  op: "Floor"
  input: "warping_model/apply_transformation/interpolate/mul_3"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/Cast_3"
  op: "Cast"
  input: "warping_model/apply_transformation/interpolate/Floor_1"
  attr {
    key: "DstT"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "SrcT"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/add_3/y"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
        }
        int_val: 1
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/add_3"
  op: "Add"
  input: "warping_model/apply_transformation/interpolate/Cast_3"
  input: "warping_model/apply_transformation/interpolate/add_3/y"
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/sub/y"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
        }
        int_val: 1
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/sub"
  op: "Sub"
  input: "warping_model/apply_transformation/interpolate/strided_slice_1"
  input: "warping_model/apply_transformation/interpolate/sub/y"
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/sub_1/y"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
        }
        int_val: 1
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/sub_1"
  op: "Sub"
  input: "warping_model/apply_transformation/interpolate/strided_slice_2"
  input: "warping_model/apply_transformation/interpolate/sub_1/y"
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/zeros"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
        }
        int_val: 0
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/clip_by_value/Minimum"
  op: "Minimum"
  input: "warping_model/apply_transformation/interpolate/Cast_2"
  input: "warping_model/apply_transformation/interpolate/sub_1"
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/clip_by_value"
  op: "Maximum"
  input: "warping_model/apply_transformation/interpolate/clip_by_value/Minimum"
  input: "warping_model/apply_transformation/interpolate/zeros"
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/clip_by_value_1/Minimum"
  op: "Minimum"
  input: "warping_model/apply_transformation/interpolate/add_2"
  input: "warping_model/apply_transformation/interpolate/sub_1"
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/clip_by_value_1"
  op: "Maximum"
  input: "warping_model/apply_transformation/interpolate/clip_by_value_1/Minimum"
  input: "warping_model/apply_transformation/interpolate/zeros"
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/clip_by_value_2/Minimum"
  op: "Minimum"
  input: "warping_model/apply_transformation/interpolate/Cast_3"
  input: "warping_model/apply_transformation/interpolate/sub"
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/clip_by_value_2"
  op: "Maximum"
  input: "warping_model/apply_transformation/interpolate/clip_by_value_2/Minimum"
  input: "warping_model/apply_transformation/interpolate/zeros"
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/clip_by_value_3/Minimum"
  op: "Minimum"
  input: "warping_model/apply_transformation/interpolate/add_3"
  input: "warping_model/apply_transformation/interpolate/sub"
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/clip_by_value_3"
  op: "Maximum"
  input: "warping_model/apply_transformation/interpolate/clip_by_value_3/Minimum"
  input: "warping_model/apply_transformation/interpolate/zeros"
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/mul_4"
  op: "Mul"
  input: "warping_model/apply_transformation/interpolate/strided_slice_1"
  input: "warping_model/apply_transformation/interpolate/strided_slice_2"
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/range/start"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
        }
        int_val: 0
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/range/delta"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
        }
        int_val: 1
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/range"
  op: "Range"
  input: "warping_model/apply_transformation/interpolate/range/start"
  input: "warping_model/apply_transformation/interpolate/strided_slice"
  input: "warping_model/apply_transformation/interpolate/range/delta"
  attr {
    key: "Tidx"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/mul_5"
  op: "Mul"
  input: "warping_model/apply_transformation/interpolate/range"
  input: "warping_model/apply_transformation/interpolate/mul_4"
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/mul_6"
  op: "Mul"
  input: "warping_model/apply_transformation/strided_slice_1"
  input: "warping_model/apply_transformation/strided_slice_2"
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/repeat/ones/mul/x"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
        }
        int_val: 1
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/repeat/ones/mul"
  op: "Mul"
  input: "warping_model/apply_transformation/interpolate/repeat/ones/mul/x"
  input: "warping_model/apply_transformation/interpolate/mul_6"
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/repeat/ones/Less/y"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
        }
        int_val: 1000
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/repeat/ones/Less"
  op: "Less"
  input: "warping_model/apply_transformation/interpolate/repeat/ones/mul"
  input: "warping_model/apply_transformation/interpolate/repeat/ones/Less/y"
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/repeat/ones/packed/0"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
        }
        int_val: 1
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/repeat/ones/packed"
  op: "Pack"
  input: "warping_model/apply_transformation/interpolate/repeat/ones/packed/0"
  input: "warping_model/apply_transformation/interpolate/mul_6"
  attr {
    key: "N"
    value {
      i: 2
    }
  }
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "axis"
    value {
      i: 0
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/repeat/ones/Const"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
        }
        int_val: 1
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/repeat/ones"
  op: "Fill"
  input: "warping_model/apply_transformation/interpolate/repeat/ones/packed"
  input: "warping_model/apply_transformation/interpolate/repeat/ones/Const"
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "index_type"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/repeat/Reshape/shape"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 2
          }
        }
        tensor_content: "\377\377\377\377\001\000\000\000"
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/repeat/Reshape"
  op: "Reshape"
  input: "warping_model/apply_transformation/interpolate/mul_5"
  input: "warping_model/apply_transformation/interpolate/repeat/Reshape/shape"
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "Tshape"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/repeat/MatMul"
  op: "MatMul"
  input: "warping_model/apply_transformation/interpolate/repeat/Reshape"
  input: "warping_model/apply_transformation/interpolate/repeat/ones"
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "transpose_a"
    value {
      b: false
    }
  }
  attr {
    key: "transpose_b"
    value {
      b: false
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/repeat/Reshape_1/shape"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 1
          }
        }
        int_val: -1
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/repeat/Reshape_1"
  op: "Reshape"
  input: "warping_model/apply_transformation/interpolate/repeat/MatMul"
  input: "warping_model/apply_transformation/interpolate/repeat/Reshape_1/shape"
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "Tshape"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/mul_7"
  op: "Mul"
  input: "warping_model/apply_transformation/interpolate/clip_by_value_2"
  input: "warping_model/apply_transformation/interpolate/strided_slice_2"
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/add_4"
  op: "Add"
  input: "warping_model/apply_transformation/interpolate/repeat/Reshape_1"
  input: "warping_model/apply_transformation/interpolate/mul_7"
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/mul_8"
  op: "Mul"
  input: "warping_model/apply_transformation/interpolate/clip_by_value_3"
  input: "warping_model/apply_transformation/interpolate/strided_slice_2"
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/add_5"
  op: "Add"
  input: "warping_model/apply_transformation/interpolate/repeat/Reshape_1"
  input: "warping_model/apply_transformation/interpolate/mul_8"
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/add_6"
  op: "Add"
  input: "warping_model/apply_transformation/interpolate/add_4"
  input: "warping_model/apply_transformation/interpolate/clip_by_value"
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/add_7"
  op: "Add"
  input: "warping_model/apply_transformation/interpolate/add_5"
  input: "warping_model/apply_transformation/interpolate/clip_by_value"
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/add_8"
  op: "Add"
  input: "warping_model/apply_transformation/interpolate/add_4"
  input: "warping_model/apply_transformation/interpolate/clip_by_value_1"
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/add_9"
  op: "Add"
  input: "warping_model/apply_transformation/interpolate/add_5"
  input: "warping_model/apply_transformation/interpolate/clip_by_value_1"
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/Reshape/shape/0"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
        }
        int_val: -1
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/Reshape/shape"
  op: "Pack"
  input: "warping_model/apply_transformation/interpolate/Reshape/shape/0"
  input: "warping_model/apply_transformation/interpolate/strided_slice_3"
  attr {
    key: "N"
    value {
      i: 2
    }
  }
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "axis"
    value {
      i: 0
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/Reshape"
  op: "Reshape"
  input: "inputs/input_img"
  input: "warping_model/apply_transformation/interpolate/Reshape/shape"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "Tshape"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/GatherV2/axis"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
        }
        int_val: 0
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/GatherV2"
  op: "GatherV2"
  input: "warping_model/apply_transformation/interpolate/Reshape"
  input: "warping_model/apply_transformation/interpolate/add_6"
  input: "warping_model/apply_transformation/interpolate/GatherV2/axis"
  attr {
    key: "Taxis"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "Tindices"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "Tparams"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/GatherV2_1/axis"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
        }
        int_val: 0
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/GatherV2_1"
  op: "GatherV2"
  input: "warping_model/apply_transformation/interpolate/Reshape"
  input: "warping_model/apply_transformation/interpolate/add_7"
  input: "warping_model/apply_transformation/interpolate/GatherV2_1/axis"
  attr {
    key: "Taxis"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "Tindices"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "Tparams"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/GatherV2_2/axis"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
        }
        int_val: 0
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/GatherV2_2"
  op: "GatherV2"
  input: "warping_model/apply_transformation/interpolate/Reshape"
  input: "warping_model/apply_transformation/interpolate/add_8"
  input: "warping_model/apply_transformation/interpolate/GatherV2_2/axis"
  attr {
    key: "Taxis"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "Tindices"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "Tparams"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/GatherV2_3/axis"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
        }
        int_val: 0
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/GatherV2_3"
  op: "GatherV2"
  input: "warping_model/apply_transformation/interpolate/Reshape"
  input: "warping_model/apply_transformation/interpolate/add_9"
  input: "warping_model/apply_transformation/interpolate/GatherV2_3/axis"
  attr {
    key: "Taxis"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "Tindices"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "Tparams"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/Cast_4"
  op: "Cast"
  input: "warping_model/apply_transformation/interpolate/clip_by_value"
  attr {
    key: "DstT"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "SrcT"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/Cast_5"
  op: "Cast"
  input: "warping_model/apply_transformation/interpolate/clip_by_value_1"
  attr {
    key: "DstT"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "SrcT"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/Cast_6"
  op: "Cast"
  input: "warping_model/apply_transformation/interpolate/clip_by_value_2"
  attr {
    key: "DstT"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "SrcT"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/Cast_7"
  op: "Cast"
  input: "warping_model/apply_transformation/interpolate/clip_by_value_3"
  attr {
    key: "DstT"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "SrcT"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/sub_2"
  op: "Sub"
  input: "warping_model/apply_transformation/interpolate/Cast_5"
  input: "warping_model/apply_transformation/interpolate/mul_1"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/sub_3"
  op: "Sub"
  input: "warping_model/apply_transformation/interpolate/Cast_7"
  input: "warping_model/apply_transformation/interpolate/mul_3"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/mul_9"
  op: "Mul"
  input: "warping_model/apply_transformation/interpolate/sub_2"
  input: "warping_model/apply_transformation/interpolate/sub_3"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/ExpandDims/dim"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
        }
        int_val: 1
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/ExpandDims"
  op: "ExpandDims"
  input: "warping_model/apply_transformation/interpolate/mul_9"
  input: "warping_model/apply_transformation/interpolate/ExpandDims/dim"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "Tdim"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/sub_4"
  op: "Sub"
  input: "warping_model/apply_transformation/interpolate/Cast_5"
  input: "warping_model/apply_transformation/interpolate/mul_1"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/sub_5"
  op: "Sub"
  input: "warping_model/apply_transformation/interpolate/mul_3"
  input: "warping_model/apply_transformation/interpolate/Cast_6"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/mul_10"
  op: "Mul"
  input: "warping_model/apply_transformation/interpolate/sub_4"
  input: "warping_model/apply_transformation/interpolate/sub_5"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/ExpandDims_1/dim"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
        }
        int_val: 1
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/ExpandDims_1"
  op: "ExpandDims"
  input: "warping_model/apply_transformation/interpolate/mul_10"
  input: "warping_model/apply_transformation/interpolate/ExpandDims_1/dim"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "Tdim"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/sub_6"
  op: "Sub"
  input: "warping_model/apply_transformation/interpolate/mul_1"
  input: "warping_model/apply_transformation/interpolate/Cast_4"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/sub_7"
  op: "Sub"
  input: "warping_model/apply_transformation/interpolate/Cast_7"
  input: "warping_model/apply_transformation/interpolate/mul_3"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/mul_11"
  op: "Mul"
  input: "warping_model/apply_transformation/interpolate/sub_6"
  input: "warping_model/apply_transformation/interpolate/sub_7"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/ExpandDims_2/dim"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
        }
        int_val: 1
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/ExpandDims_2"
  op: "ExpandDims"
  input: "warping_model/apply_transformation/interpolate/mul_11"
  input: "warping_model/apply_transformation/interpolate/ExpandDims_2/dim"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "Tdim"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/sub_8"
  op: "Sub"
  input: "warping_model/apply_transformation/interpolate/mul_1"
  input: "warping_model/apply_transformation/interpolate/Cast_4"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/sub_9"
  op: "Sub"
  input: "warping_model/apply_transformation/interpolate/mul_3"
  input: "warping_model/apply_transformation/interpolate/Cast_6"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/mul_12"
  op: "Mul"
  input: "warping_model/apply_transformation/interpolate/sub_8"
  input: "warping_model/apply_transformation/interpolate/sub_9"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/ExpandDims_3/dim"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
        }
        int_val: 1
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/ExpandDims_3"
  op: "ExpandDims"
  input: "warping_model/apply_transformation/interpolate/mul_12"
  input: "warping_model/apply_transformation/interpolate/ExpandDims_3/dim"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "Tdim"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/mul_13"
  op: "Mul"
  input: "warping_model/apply_transformation/interpolate/ExpandDims"
  input: "warping_model/apply_transformation/interpolate/GatherV2"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/mul_14"
  op: "Mul"
  input: "warping_model/apply_transformation/interpolate/ExpandDims_1"
  input: "warping_model/apply_transformation/interpolate/GatherV2_1"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/mul_15"
  op: "Mul"
  input: "warping_model/apply_transformation/interpolate/ExpandDims_2"
  input: "warping_model/apply_transformation/interpolate/GatherV2_2"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/mul_16"
  op: "Mul"
  input: "warping_model/apply_transformation/interpolate/ExpandDims_3"
  input: "warping_model/apply_transformation/interpolate/GatherV2_3"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/apply_transformation/interpolate/AddN"
  op: "AddN"
  input: "warping_model/apply_transformation/interpolate/mul_13"
  input: "warping_model/apply_transformation/interpolate/mul_14"
  input: "warping_model/apply_transformation/interpolate/mul_15"
  input: "warping_model/apply_transformation/interpolate/mul_16"
  attr {
    key: "N"
    value {
      i: 4
    }
  }
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/apply_transformation/Reshape_3/shape/3"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
        }
        int_val: 3
      }
    }
  }
}
node {
  name: "warping_model/apply_transformation/Reshape_3/shape"
  op: "Pack"
  input: "warping_model/apply_transformation/strided_slice"
  input: "warping_model/apply_transformation/strided_slice_1"
  input: "warping_model/apply_transformation/strided_slice_2"
  input: "warping_model/apply_transformation/Reshape_3/shape/3"
  attr {
    key: "N"
    value {
      i: 4
    }
  }
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "axis"
    value {
      i: 0
    }
  }
}
node {
  name: "warping_model/apply_transformation/Reshape_3"
  op: "Reshape"
  input: "warping_model/apply_transformation/interpolate/AddN"
  input: "warping_model/apply_transformation/Reshape_3/shape"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "Tshape"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/cnn/kernel/Initializer/random_uniform/shape"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_0/cnn/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 4
          }
        }
        tensor_content: "\003\000\000\000\003\000\000\000\002\000\000\000\010\000\000\000"
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/cnn/kernel/Initializer/random_uniform/min"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_0/cnn/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: -0.25819888710975647
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/cnn/kernel/Initializer/random_uniform/max"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_0/cnn/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 0.25819888710975647
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/cnn/kernel/Initializer/random_uniform/RandomUniform"
  op: "RandomUniform"
  input: "warping_model/lcm_module/cnn_blk_0/cnn/kernel/Initializer/random_uniform/shape"
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_0/cnn/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "seed"
    value {
      i: 0
    }
  }
  attr {
    key: "seed2"
    value {
      i: 0
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/cnn/kernel/Initializer/random_uniform/sub"
  op: "Sub"
  input: "warping_model/lcm_module/cnn_blk_0/cnn/kernel/Initializer/random_uniform/max"
  input: "warping_model/lcm_module/cnn_blk_0/cnn/kernel/Initializer/random_uniform/min"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_0/cnn/kernel"
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/cnn/kernel/Initializer/random_uniform/mul"
  op: "Mul"
  input: "warping_model/lcm_module/cnn_blk_0/cnn/kernel/Initializer/random_uniform/RandomUniform"
  input: "warping_model/lcm_module/cnn_blk_0/cnn/kernel/Initializer/random_uniform/sub"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_0/cnn/kernel"
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/cnn/kernel/Initializer/random_uniform"
  op: "Add"
  input: "warping_model/lcm_module/cnn_blk_0/cnn/kernel/Initializer/random_uniform/mul"
  input: "warping_model/lcm_module/cnn_blk_0/cnn/kernel/Initializer/random_uniform/min"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_0/cnn/kernel"
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/cnn/kernel"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_0/cnn/kernel"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 3
        }
        dim {
          size: 3
        }
        dim {
          size: 2
        }
        dim {
          size: 8
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/cnn/kernel/Assign"
  op: "Assign"
  input: "warping_model/lcm_module/cnn_blk_0/cnn/kernel"
  input: "warping_model/lcm_module/cnn_blk_0/cnn/kernel/Initializer/random_uniform"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_0/cnn/kernel"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/cnn/kernel/read"
  op: "Identity"
  input: "warping_model/lcm_module/cnn_blk_0/cnn/kernel"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_0/cnn/kernel"
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/cnn/dilation_rate"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 2
          }
        }
        tensor_content: "\001\000\000\000\001\000\000\000"
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/cnn/Conv2D"
  op: "Conv2D"
  input: "warping_model/warping_module/split:1"
  input: "warping_model/lcm_module/cnn_blk_0/cnn/kernel/read"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "data_format"
    value {
      s: "NHWC"
    }
  }
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "use_cudnn_on_gpu"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/act"
  op: "Relu"
  input: "warping_model/lcm_module/cnn_blk_0/cnn/Conv2D"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/bn_layer/gamma/Initializer/ones"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_0/bn_layer/gamma"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 8
          }
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/bn_layer/gamma"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_0/bn_layer/gamma"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 8
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/bn_layer/gamma/Assign"
  op: "Assign"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/gamma"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/gamma/Initializer/ones"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_0/bn_layer/gamma"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/bn_layer/gamma/read"
  op: "Identity"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/gamma"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_0/bn_layer/gamma"
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/bn_layer/beta/Initializer/zeros"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_0/bn_layer/beta"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 8
          }
        }
        float_val: 0.0
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/bn_layer/beta"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_0/bn_layer/beta"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 8
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/bn_layer/beta/Assign"
  op: "Assign"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/beta"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/beta/Initializer/zeros"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_0/bn_layer/beta"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/bn_layer/beta/read"
  op: "Identity"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/beta"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_0/bn_layer/beta"
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/bn_layer/moving_mean/Initializer/zeros"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_0/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 8
          }
        }
        float_val: 0.0
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/bn_layer/moving_mean"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_0/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 8
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/bn_layer/moving_mean/Assign"
  op: "Assign"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/moving_mean"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/moving_mean/Initializer/zeros"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_0/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/bn_layer/moving_mean/read"
  op: "Identity"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/moving_mean"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_0/bn_layer/moving_mean"
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/bn_layer/moving_variance/Initializer/ones"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_0/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 8
          }
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/bn_layer/moving_variance"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_0/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 8
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/bn_layer/moving_variance/Assign"
  op: "Assign"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/moving_variance"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/moving_variance/Initializer/ones"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_0/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/bn_layer/moving_variance/read"
  op: "Identity"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/moving_variance"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_0/bn_layer/moving_variance"
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond/Switch"
  op: "Switch"
  input: "inputs/phase_train"
  input: "inputs/phase_train"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond/switch_t"
  op: "Identity"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond/Switch:1"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond/switch_f"
  op: "Identity"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond/Switch"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond/pred_id"
  op: "Identity"
  input: "inputs/phase_train"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond/Const"
  op: "Const"
  input: "^warping_model/lcm_module/cnn_blk_0/bn_layer/cond/switch_t"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
          }
        }
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond/Const_1"
  op: "Const"
  input: "^warping_model/lcm_module/cnn_blk_0/bn_layer/cond/switch_t"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
          }
        }
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond/FusedBatchNorm"
  op: "FusedBatchNorm"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond/FusedBatchNorm/Switch:1"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond/FusedBatchNorm/Switch_1:1"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond/FusedBatchNorm/Switch_2:1"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond/Const"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond/Const_1"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "data_format"
    value {
      s: "NHWC"
    }
  }
  attr {
    key: "epsilon"
    value {
      f: 1.0009999641624745e-05
    }
  }
  attr {
    key: "is_training"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond/FusedBatchNorm/Switch"
  op: "Switch"
  input: "warping_model/lcm_module/cnn_blk_0/act"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_0/act"
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond/FusedBatchNorm/Switch_1"
  op: "Switch"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/gamma/read"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_0/bn_layer/gamma"
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond/FusedBatchNorm/Switch_2"
  op: "Switch"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/beta/read"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_0/bn_layer/beta"
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond/FusedBatchNorm_1"
  op: "FusedBatchNorm"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond/FusedBatchNorm_1/Switch"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond/FusedBatchNorm_1/Switch_1"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond/FusedBatchNorm_1/Switch_2"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond/FusedBatchNorm_1/Switch_3"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond/FusedBatchNorm_1/Switch_4"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "data_format"
    value {
      s: "NHWC"
    }
  }
  attr {
    key: "epsilon"
    value {
      f: 1.0009999641624745e-05
    }
  }
  attr {
    key: "is_training"
    value {
      b: false
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond/FusedBatchNorm_1/Switch"
  op: "Switch"
  input: "warping_model/lcm_module/cnn_blk_0/act"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_0/act"
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond/FusedBatchNorm_1/Switch_1"
  op: "Switch"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/gamma/read"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_0/bn_layer/gamma"
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond/FusedBatchNorm_1/Switch_2"
  op: "Switch"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/beta/read"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_0/bn_layer/beta"
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond/FusedBatchNorm_1/Switch_3"
  op: "Switch"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/moving_mean/read"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_0/bn_layer/moving_mean"
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond/FusedBatchNorm_1/Switch_4"
  op: "Switch"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/moving_variance/read"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_0/bn_layer/moving_variance"
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond/Merge"
  op: "Merge"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond/FusedBatchNorm_1"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond/FusedBatchNorm"
  attr {
    key: "N"
    value {
      i: 2
    }
  }
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond/Merge_1"
  op: "Merge"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond/FusedBatchNorm_1:1"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond/FusedBatchNorm:1"
  attr {
    key: "N"
    value {
      i: 2
    }
  }
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond/Merge_2"
  op: "Merge"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond/FusedBatchNorm_1:2"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond/FusedBatchNorm:2"
  attr {
    key: "N"
    value {
      i: 2
    }
  }
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond_1/Switch"
  op: "Switch"
  input: "inputs/phase_train"
  input: "inputs/phase_train"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond_1/switch_t"
  op: "Identity"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond_1/Switch:1"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond_1/switch_f"
  op: "Identity"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond_1/Switch"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond_1/pred_id"
  op: "Identity"
  input: "inputs/phase_train"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond_1/Const"
  op: "Const"
  input: "^warping_model/lcm_module/cnn_blk_0/bn_layer/cond_1/switch_t"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 0.8999999761581421
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond_1/Const_1"
  op: "Const"
  input: "^warping_model/lcm_module/cnn_blk_0/bn_layer/cond_1/switch_f"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond_1/Merge"
  op: "Merge"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond_1/Const_1"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond_1/Const"
  attr {
    key: "N"
    value {
      i: 2
    }
  }
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/bn_layer/AssignMovingAvg/sub/x"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_0/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/bn_layer/AssignMovingAvg/sub"
  op: "Sub"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/AssignMovingAvg/sub/x"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond_1/Merge"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_0/bn_layer/moving_mean"
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/bn_layer/AssignMovingAvg/sub_1"
  op: "Sub"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/moving_mean/read"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond/Merge_1"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_0/bn_layer/moving_mean"
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/bn_layer/AssignMovingAvg/mul"
  op: "Mul"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/AssignMovingAvg/sub_1"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/AssignMovingAvg/sub"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_0/bn_layer/moving_mean"
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/bn_layer/AssignMovingAvg"
  op: "AssignSub"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/moving_mean"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/AssignMovingAvg/mul"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_0/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: false
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/bn_layer/AssignMovingAvg_1/sub/x"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_0/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/bn_layer/AssignMovingAvg_1/sub"
  op: "Sub"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/AssignMovingAvg_1/sub/x"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond_1/Merge"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_0/bn_layer/moving_variance"
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/bn_layer/AssignMovingAvg_1/sub_1"
  op: "Sub"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/moving_variance/read"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond/Merge_2"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_0/bn_layer/moving_variance"
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/bn_layer/AssignMovingAvg_1/mul"
  op: "Mul"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/AssignMovingAvg_1/sub_1"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/AssignMovingAvg_1/sub"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_0/bn_layer/moving_variance"
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_0/bn_layer/AssignMovingAvg_1"
  op: "AssignSub"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/moving_variance"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/AssignMovingAvg_1/mul"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_0/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: false
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/cnn/kernel/Initializer/random_uniform/shape"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_1/cnn/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 4
          }
        }
        tensor_content: "\003\000\000\000\003\000\000\000\010\000\000\000\010\000\000\000"
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/cnn/kernel/Initializer/random_uniform/min"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_1/cnn/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: -0.20412415266036987
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/cnn/kernel/Initializer/random_uniform/max"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_1/cnn/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 0.20412415266036987
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/cnn/kernel/Initializer/random_uniform/RandomUniform"
  op: "RandomUniform"
  input: "warping_model/lcm_module/cnn_blk_1/cnn/kernel/Initializer/random_uniform/shape"
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_1/cnn/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "seed"
    value {
      i: 0
    }
  }
  attr {
    key: "seed2"
    value {
      i: 0
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/cnn/kernel/Initializer/random_uniform/sub"
  op: "Sub"
  input: "warping_model/lcm_module/cnn_blk_1/cnn/kernel/Initializer/random_uniform/max"
  input: "warping_model/lcm_module/cnn_blk_1/cnn/kernel/Initializer/random_uniform/min"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_1/cnn/kernel"
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/cnn/kernel/Initializer/random_uniform/mul"
  op: "Mul"
  input: "warping_model/lcm_module/cnn_blk_1/cnn/kernel/Initializer/random_uniform/RandomUniform"
  input: "warping_model/lcm_module/cnn_blk_1/cnn/kernel/Initializer/random_uniform/sub"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_1/cnn/kernel"
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/cnn/kernel/Initializer/random_uniform"
  op: "Add"
  input: "warping_model/lcm_module/cnn_blk_1/cnn/kernel/Initializer/random_uniform/mul"
  input: "warping_model/lcm_module/cnn_blk_1/cnn/kernel/Initializer/random_uniform/min"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_1/cnn/kernel"
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/cnn/kernel"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_1/cnn/kernel"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 3
        }
        dim {
          size: 3
        }
        dim {
          size: 8
        }
        dim {
          size: 8
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/cnn/kernel/Assign"
  op: "Assign"
  input: "warping_model/lcm_module/cnn_blk_1/cnn/kernel"
  input: "warping_model/lcm_module/cnn_blk_1/cnn/kernel/Initializer/random_uniform"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_1/cnn/kernel"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/cnn/kernel/read"
  op: "Identity"
  input: "warping_model/lcm_module/cnn_blk_1/cnn/kernel"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_1/cnn/kernel"
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/cnn/dilation_rate"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 2
          }
        }
        tensor_content: "\001\000\000\000\001\000\000\000"
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/cnn/Conv2D"
  op: "Conv2D"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/cond/Merge"
  input: "warping_model/lcm_module/cnn_blk_1/cnn/kernel/read"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "data_format"
    value {
      s: "NHWC"
    }
  }
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "use_cudnn_on_gpu"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/act"
  op: "Relu"
  input: "warping_model/lcm_module/cnn_blk_1/cnn/Conv2D"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/bn_layer/gamma/Initializer/ones"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_1/bn_layer/gamma"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 8
          }
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/bn_layer/gamma"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_1/bn_layer/gamma"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 8
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/bn_layer/gamma/Assign"
  op: "Assign"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/gamma"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/gamma/Initializer/ones"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_1/bn_layer/gamma"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/bn_layer/gamma/read"
  op: "Identity"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/gamma"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_1/bn_layer/gamma"
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/bn_layer/beta/Initializer/zeros"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_1/bn_layer/beta"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 8
          }
        }
        float_val: 0.0
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/bn_layer/beta"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_1/bn_layer/beta"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 8
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/bn_layer/beta/Assign"
  op: "Assign"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/beta"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/beta/Initializer/zeros"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_1/bn_layer/beta"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/bn_layer/beta/read"
  op: "Identity"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/beta"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_1/bn_layer/beta"
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/bn_layer/moving_mean/Initializer/zeros"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_1/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 8
          }
        }
        float_val: 0.0
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/bn_layer/moving_mean"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_1/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 8
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/bn_layer/moving_mean/Assign"
  op: "Assign"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/moving_mean"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/moving_mean/Initializer/zeros"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_1/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/bn_layer/moving_mean/read"
  op: "Identity"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/moving_mean"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_1/bn_layer/moving_mean"
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/bn_layer/moving_variance/Initializer/ones"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_1/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 8
          }
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/bn_layer/moving_variance"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_1/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 8
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/bn_layer/moving_variance/Assign"
  op: "Assign"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/moving_variance"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/moving_variance/Initializer/ones"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_1/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/bn_layer/moving_variance/read"
  op: "Identity"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/moving_variance"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_1/bn_layer/moving_variance"
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond/Switch"
  op: "Switch"
  input: "inputs/phase_train"
  input: "inputs/phase_train"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond/switch_t"
  op: "Identity"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond/Switch:1"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond/switch_f"
  op: "Identity"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond/Switch"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond/pred_id"
  op: "Identity"
  input: "inputs/phase_train"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond/Const"
  op: "Const"
  input: "^warping_model/lcm_module/cnn_blk_1/bn_layer/cond/switch_t"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
          }
        }
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond/Const_1"
  op: "Const"
  input: "^warping_model/lcm_module/cnn_blk_1/bn_layer/cond/switch_t"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
          }
        }
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond/FusedBatchNorm"
  op: "FusedBatchNorm"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond/FusedBatchNorm/Switch:1"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond/FusedBatchNorm/Switch_1:1"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond/FusedBatchNorm/Switch_2:1"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond/Const"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond/Const_1"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "data_format"
    value {
      s: "NHWC"
    }
  }
  attr {
    key: "epsilon"
    value {
      f: 1.0009999641624745e-05
    }
  }
  attr {
    key: "is_training"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond/FusedBatchNorm/Switch"
  op: "Switch"
  input: "warping_model/lcm_module/cnn_blk_1/act"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_1/act"
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond/FusedBatchNorm/Switch_1"
  op: "Switch"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/gamma/read"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_1/bn_layer/gamma"
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond/FusedBatchNorm/Switch_2"
  op: "Switch"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/beta/read"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_1/bn_layer/beta"
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond/FusedBatchNorm_1"
  op: "FusedBatchNorm"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond/FusedBatchNorm_1/Switch"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond/FusedBatchNorm_1/Switch_1"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond/FusedBatchNorm_1/Switch_2"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond/FusedBatchNorm_1/Switch_3"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond/FusedBatchNorm_1/Switch_4"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "data_format"
    value {
      s: "NHWC"
    }
  }
  attr {
    key: "epsilon"
    value {
      f: 1.0009999641624745e-05
    }
  }
  attr {
    key: "is_training"
    value {
      b: false
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond/FusedBatchNorm_1/Switch"
  op: "Switch"
  input: "warping_model/lcm_module/cnn_blk_1/act"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_1/act"
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond/FusedBatchNorm_1/Switch_1"
  op: "Switch"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/gamma/read"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_1/bn_layer/gamma"
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond/FusedBatchNorm_1/Switch_2"
  op: "Switch"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/beta/read"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_1/bn_layer/beta"
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond/FusedBatchNorm_1/Switch_3"
  op: "Switch"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/moving_mean/read"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_1/bn_layer/moving_mean"
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond/FusedBatchNorm_1/Switch_4"
  op: "Switch"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/moving_variance/read"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond/pred_id"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_1/bn_layer/moving_variance"
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond/Merge"
  op: "Merge"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond/FusedBatchNorm_1"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond/FusedBatchNorm"
  attr {
    key: "N"
    value {
      i: 2
    }
  }
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond/Merge_1"
  op: "Merge"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond/FusedBatchNorm_1:1"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond/FusedBatchNorm:1"
  attr {
    key: "N"
    value {
      i: 2
    }
  }
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond/Merge_2"
  op: "Merge"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond/FusedBatchNorm_1:2"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond/FusedBatchNorm:2"
  attr {
    key: "N"
    value {
      i: 2
    }
  }
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond_1/Switch"
  op: "Switch"
  input: "inputs/phase_train"
  input: "inputs/phase_train"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond_1/switch_t"
  op: "Identity"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond_1/Switch:1"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond_1/switch_f"
  op: "Identity"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond_1/Switch"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond_1/pred_id"
  op: "Identity"
  input: "inputs/phase_train"
  attr {
    key: "T"
    value {
      type: DT_BOOL
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond_1/Const"
  op: "Const"
  input: "^warping_model/lcm_module/cnn_blk_1/bn_layer/cond_1/switch_t"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 0.8999999761581421
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond_1/Const_1"
  op: "Const"
  input: "^warping_model/lcm_module/cnn_blk_1/bn_layer/cond_1/switch_f"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond_1/Merge"
  op: "Merge"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond_1/Const_1"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond_1/Const"
  attr {
    key: "N"
    value {
      i: 2
    }
  }
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/bn_layer/AssignMovingAvg/sub/x"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_1/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/bn_layer/AssignMovingAvg/sub"
  op: "Sub"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/AssignMovingAvg/sub/x"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond_1/Merge"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_1/bn_layer/moving_mean"
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/bn_layer/AssignMovingAvg/sub_1"
  op: "Sub"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/moving_mean/read"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond/Merge_1"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_1/bn_layer/moving_mean"
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/bn_layer/AssignMovingAvg/mul"
  op: "Mul"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/AssignMovingAvg/sub_1"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/AssignMovingAvg/sub"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_1/bn_layer/moving_mean"
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/bn_layer/AssignMovingAvg"
  op: "AssignSub"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/moving_mean"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/AssignMovingAvg/mul"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_1/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: false
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/bn_layer/AssignMovingAvg_1/sub/x"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_1/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/bn_layer/AssignMovingAvg_1/sub"
  op: "Sub"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/AssignMovingAvg_1/sub/x"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond_1/Merge"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_1/bn_layer/moving_variance"
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/bn_layer/AssignMovingAvg_1/sub_1"
  op: "Sub"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/moving_variance/read"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond/Merge_2"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_1/bn_layer/moving_variance"
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/bn_layer/AssignMovingAvg_1/mul"
  op: "Mul"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/AssignMovingAvg_1/sub_1"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/AssignMovingAvg_1/sub"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_1/bn_layer/moving_variance"
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_blk_1/bn_layer/AssignMovingAvg_1"
  op: "AssignSub"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/moving_variance"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/AssignMovingAvg_1/mul"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_1/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: false
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_2/kernel/Initializer/random_uniform/shape"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_2/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 4
          }
        }
        tensor_content: "\001\000\000\000\001\000\000\000\010\000\000\000\002\000\000\000"
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_2/kernel/Initializer/random_uniform/min"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_2/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: -0.7745966911315918
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_2/kernel/Initializer/random_uniform/max"
  op: "Const"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_2/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 0.7745966911315918
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_2/kernel/Initializer/random_uniform/RandomUniform"
  op: "RandomUniform"
  input: "warping_model/lcm_module/cnn_2/kernel/Initializer/random_uniform/shape"
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_2/kernel"
      }
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "seed"
    value {
      i: 0
    }
  }
  attr {
    key: "seed2"
    value {
      i: 0
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_2/kernel/Initializer/random_uniform/sub"
  op: "Sub"
  input: "warping_model/lcm_module/cnn_2/kernel/Initializer/random_uniform/max"
  input: "warping_model/lcm_module/cnn_2/kernel/Initializer/random_uniform/min"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_2/kernel"
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_2/kernel/Initializer/random_uniform/mul"
  op: "Mul"
  input: "warping_model/lcm_module/cnn_2/kernel/Initializer/random_uniform/RandomUniform"
  input: "warping_model/lcm_module/cnn_2/kernel/Initializer/random_uniform/sub"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_2/kernel"
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_2/kernel/Initializer/random_uniform"
  op: "Add"
  input: "warping_model/lcm_module/cnn_2/kernel/Initializer/random_uniform/mul"
  input: "warping_model/lcm_module/cnn_2/kernel/Initializer/random_uniform/min"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_2/kernel"
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_2/kernel"
  op: "VariableV2"
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_2/kernel"
      }
    }
  }
  attr {
    key: "container"
    value {
      s: ""
    }
  }
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
        dim {
          size: 1
        }
        dim {
          size: 1
        }
        dim {
          size: 8
        }
        dim {
          size: 2
        }
      }
    }
  }
  attr {
    key: "shared_name"
    value {
      s: ""
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_2/kernel/Assign"
  op: "Assign"
  input: "warping_model/lcm_module/cnn_2/kernel"
  input: "warping_model/lcm_module/cnn_2/kernel/Initializer/random_uniform"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_2/kernel"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_2/kernel/read"
  op: "Identity"
  input: "warping_model/lcm_module/cnn_2/kernel"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_2/kernel"
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_2/dilation_rate"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 2
          }
        }
        tensor_content: "\001\000\000\000\001\000\000\000"
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/cnn_2/Conv2D"
  op: "Conv2D"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/cond/Merge"
  input: "warping_model/lcm_module/cnn_2/kernel/read"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "data_format"
    value {
      s: "NHWC"
    }
  }
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "use_cudnn_on_gpu"
    value {
      b: true
    }
  }
}
node {
  name: "warping_model/lcm_module/Shape"
  op: "Shape"
  input: "warping_model/lcm_module/cnn_2/Conv2D"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "out_type"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/lcm_module/Rank"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
        }
        int_val: 4
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/Shape_1"
  op: "Shape"
  input: "warping_model/lcm_module/cnn_2/Conv2D"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "out_type"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/lcm_module/Sub/y"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
        }
        int_val: 1
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/Sub"
  op: "Sub"
  input: "warping_model/lcm_module/Rank"
  input: "warping_model/lcm_module/Sub/y"
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/lcm_module/Slice/begin"
  op: "Pack"
  input: "warping_model/lcm_module/Sub"
  attr {
    key: "N"
    value {
      i: 1
    }
  }
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "axis"
    value {
      i: 0
    }
  }
}
node {
  name: "warping_model/lcm_module/Slice/size"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 1
          }
        }
        int_val: 1
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/Slice"
  op: "Slice"
  input: "warping_model/lcm_module/Shape_1"
  input: "warping_model/lcm_module/Slice/begin"
  input: "warping_model/lcm_module/Slice/size"
  attr {
    key: "Index"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/lcm_module/concat/values_0"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 1
          }
        }
        int_val: -1
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/concat/axis"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
        }
        int_val: 0
      }
    }
  }
}
node {
  name: "warping_model/lcm_module/concat"
  op: "ConcatV2"
  input: "warping_model/lcm_module/concat/values_0"
  input: "warping_model/lcm_module/Slice"
  input: "warping_model/lcm_module/concat/axis"
  attr {
    key: "N"
    value {
      i: 2
    }
  }
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "Tidx"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/lcm_module/Reshape"
  op: "Reshape"
  input: "warping_model/lcm_module/cnn_2/Conv2D"
  input: "warping_model/lcm_module/concat"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "Tshape"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/lcm_module/Softmax"
  op: "Softmax"
  input: "warping_model/lcm_module/Reshape"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/lcm_module/Reshape_1"
  op: "Reshape"
  input: "warping_model/lcm_module/Softmax"
  input: "warping_model/lcm_module/Shape"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "Tshape"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_lcm/Const"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 2
          }
        }
        tensor_content: "\001\000\000\000\001\000\000\000"
      }
    }
  }
}
node {
  name: "warping_model/apply_lcm/split/split_dim"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
        }
        int_val: 3
      }
    }
  }
}
node {
  name: "warping_model/apply_lcm/split"
  op: "SplitV"
  input: "warping_model/lcm_module/Reshape_1"
  input: "warping_model/apply_lcm/Const"
  input: "warping_model/apply_lcm/split/split_dim"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "Tlen"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "num_split"
    value {
      i: 2
    }
  }
}
node {
  name: "warping_model/apply_lcm/Tile/multiples"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 4
          }
        }
        tensor_content: "\001\000\000\000\001\000\000\000\001\000\000\000\003\000\000\000"
      }
    }
  }
}
node {
  name: "warping_model/apply_lcm/Tile"
  op: "Tile"
  input: "warping_model/apply_lcm/split"
  input: "warping_model/apply_lcm/Tile/multiples"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "Tmultiples"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_lcm/Tile_1/multiples"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_INT32
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 4
          }
        }
        tensor_content: "\001\000\000\000\001\000\000\000\001\000\000\000\003\000\000\000"
      }
    }
  }
}
node {
  name: "warping_model/apply_lcm/Tile_1"
  op: "Tile"
  input: "warping_model/apply_lcm/split:1"
  input: "warping_model/apply_lcm/Tile_1/multiples"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "Tmultiples"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_lcm/Shape"
  op: "Shape"
  input: "warping_model/apply_transformation/Reshape_3"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "out_type"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_lcm/ones/Const"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "warping_model/apply_lcm/ones"
  op: "Fill"
  input: "warping_model/apply_lcm/Shape"
  input: "warping_model/apply_lcm/ones/Const"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "index_type"
    value {
      type: DT_INT32
    }
  }
}
node {
  name: "warping_model/apply_lcm/Mul"
  op: "Mul"
  input: "warping_model/apply_transformation/Reshape_3"
  input: "warping_model/apply_lcm/Tile"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/apply_lcm/Mul_1"
  op: "Mul"
  input: "warping_model/apply_lcm/ones"
  input: "warping_model/apply_lcm/Tile_1"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "warping_model/apply_lcm/Add"
  op: "Add"
  input: "warping_model/apply_lcm/Mul"
  input: "warping_model/apply_lcm/Mul_1"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
node {
  name: "save/Const"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_STRING
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_STRING
        tensor_shape {
        }
        string_val: "model"
      }
    }
  }
}
node {
  name: "save/SaveV2/tensor_names"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_STRING
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_STRING
        tensor_shape {
          dim {
            size: 59
          }
        }
        string_val: "warping_model/encoder/dnn_blk_0/dnn/bias"
        string_val: "warping_model/encoder/dnn_blk_0/dnn/kernel"
        string_val: "warping_model/encoder/dnn_blk_1/dnn/bias"
        string_val: "warping_model/encoder/dnn_blk_1/dnn/kernel"
        string_val: "warping_model/encoder/dnn_blk_2/dnn/bias"
        string_val: "warping_model/encoder/dnn_blk_2/dnn/kernel"
        string_val: "warping_model/lcm_module/cnn_2/kernel"
        string_val: "warping_model/lcm_module/cnn_blk_0/bn_layer/beta"
        string_val: "warping_model/lcm_module/cnn_blk_0/bn_layer/gamma"
        string_val: "warping_model/lcm_module/cnn_blk_0/bn_layer/moving_mean"
        string_val: "warping_model/lcm_module/cnn_blk_0/bn_layer/moving_variance"
        string_val: "warping_model/lcm_module/cnn_blk_0/cnn/kernel"
        string_val: "warping_model/lcm_module/cnn_blk_1/bn_layer/beta"
        string_val: "warping_model/lcm_module/cnn_blk_1/bn_layer/gamma"
        string_val: "warping_model/lcm_module/cnn_blk_1/bn_layer/moving_mean"
        string_val: "warping_model/lcm_module/cnn_blk_1/bn_layer/moving_variance"
        string_val: "warping_model/lcm_module/cnn_blk_1/cnn/kernel"
        string_val: "warping_model/warping_module/coarse_level/cnn_4/kernel"
        string_val: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/beta"
        string_val: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/gamma"
        string_val: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/moving_mean"
        string_val: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/moving_variance"
        string_val: "warping_model/warping_module/coarse_level/cnn_blk_0/cnn/kernel"
        string_val: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/beta"
        string_val: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/gamma"
        string_val: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/moving_mean"
        string_val: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/moving_variance"
        string_val: "warping_model/warping_module/coarse_level/cnn_blk_1/cnn/kernel"
        string_val: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/beta"
        string_val: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/gamma"
        string_val: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/moving_mean"
        string_val: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/moving_variance"
        string_val: "warping_model/warping_module/coarse_level/cnn_blk_2/cnn/kernel"
        string_val: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/beta"
        string_val: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/gamma"
        string_val: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/moving_mean"
        string_val: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/moving_variance"
        string_val: "warping_model/warping_module/coarse_level/cnn_blk_3/cnn/kernel"
        string_val: "warping_model/warping_module/fine_level/cnn_4/kernel"
        string_val: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/beta"
        string_val: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/gamma"
        string_val: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/moving_mean"
        string_val: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/moving_variance"
        string_val: "warping_model/warping_module/fine_level/cnn_blk_0/cnn/kernel"
        string_val: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/beta"
        string_val: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/gamma"
        string_val: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/moving_mean"
        string_val: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/moving_variance"
        string_val: "warping_model/warping_module/fine_level/cnn_blk_1/cnn/kernel"
        string_val: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/beta"
        string_val: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/gamma"
        string_val: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/moving_mean"
        string_val: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/moving_variance"
        string_val: "warping_model/warping_module/fine_level/cnn_blk_2/cnn/kernel"
        string_val: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/beta"
        string_val: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/gamma"
        string_val: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/moving_mean"
        string_val: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/moving_variance"
        string_val: "warping_model/warping_module/fine_level/cnn_blk_3/cnn/kernel"
      }
    }
  }
}
node {
  name: "save/SaveV2/shape_and_slices"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_STRING
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_STRING
        tensor_shape {
          dim {
            size: 59
          }
        }
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
      }
    }
  }
}
node {
  name: "save/SaveV2"
  op: "SaveV2"
  input: "save/Const"
  input: "save/SaveV2/tensor_names"
  input: "save/SaveV2/shape_and_slices"
  input: "warping_model/encoder/dnn_blk_0/dnn/bias"
  input: "warping_model/encoder/dnn_blk_0/dnn/kernel"
  input: "warping_model/encoder/dnn_blk_1/dnn/bias"
  input: "warping_model/encoder/dnn_blk_1/dnn/kernel"
  input: "warping_model/encoder/dnn_blk_2/dnn/bias"
  input: "warping_model/encoder/dnn_blk_2/dnn/kernel"
  input: "warping_model/lcm_module/cnn_2/kernel"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/beta"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/gamma"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/moving_mean"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/moving_variance"
  input: "warping_model/lcm_module/cnn_blk_0/cnn/kernel"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/beta"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/gamma"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/moving_mean"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/moving_variance"
  input: "warping_model/lcm_module/cnn_blk_1/cnn/kernel"
  input: "warping_model/warping_module/coarse_level/cnn_4/kernel"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/beta"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/gamma"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/moving_mean"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/moving_variance"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/cnn/kernel"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/beta"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/gamma"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/moving_mean"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/moving_variance"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/cnn/kernel"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/beta"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/gamma"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/moving_mean"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/moving_variance"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/cnn/kernel"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/beta"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/gamma"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/moving_mean"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/moving_variance"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/cnn/kernel"
  input: "warping_model/warping_module/fine_level/cnn_4/kernel"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/beta"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/gamma"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/moving_mean"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/moving_variance"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/cnn/kernel"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/beta"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/gamma"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/moving_mean"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/moving_variance"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/cnn/kernel"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/beta"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/gamma"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/moving_mean"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/moving_variance"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/cnn/kernel"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/beta"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/gamma"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/moving_mean"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/moving_variance"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/cnn/kernel"
  attr {
    key: "dtypes"
    value {
      list {
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
      }
    }
  }
}
node {
  name: "save/control_dependency"
  op: "Identity"
  input: "save/Const"
  input: "^save/SaveV2"
  attr {
    key: "T"
    value {
      type: DT_STRING
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@save/Const"
      }
    }
  }
}
node {
  name: "save/RestoreV2/tensor_names"
  op: "Const"
  device: "/device:CPU:0"
  attr {
    key: "dtype"
    value {
      type: DT_STRING
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_STRING
        tensor_shape {
          dim {
            size: 59
          }
        }
        string_val: "warping_model/encoder/dnn_blk_0/dnn/bias"
        string_val: "warping_model/encoder/dnn_blk_0/dnn/kernel"
        string_val: "warping_model/encoder/dnn_blk_1/dnn/bias"
        string_val: "warping_model/encoder/dnn_blk_1/dnn/kernel"
        string_val: "warping_model/encoder/dnn_blk_2/dnn/bias"
        string_val: "warping_model/encoder/dnn_blk_2/dnn/kernel"
        string_val: "warping_model/lcm_module/cnn_2/kernel"
        string_val: "warping_model/lcm_module/cnn_blk_0/bn_layer/beta"
        string_val: "warping_model/lcm_module/cnn_blk_0/bn_layer/gamma"
        string_val: "warping_model/lcm_module/cnn_blk_0/bn_layer/moving_mean"
        string_val: "warping_model/lcm_module/cnn_blk_0/bn_layer/moving_variance"
        string_val: "warping_model/lcm_module/cnn_blk_0/cnn/kernel"
        string_val: "warping_model/lcm_module/cnn_blk_1/bn_layer/beta"
        string_val: "warping_model/lcm_module/cnn_blk_1/bn_layer/gamma"
        string_val: "warping_model/lcm_module/cnn_blk_1/bn_layer/moving_mean"
        string_val: "warping_model/lcm_module/cnn_blk_1/bn_layer/moving_variance"
        string_val: "warping_model/lcm_module/cnn_blk_1/cnn/kernel"
        string_val: "warping_model/warping_module/coarse_level/cnn_4/kernel"
        string_val: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/beta"
        string_val: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/gamma"
        string_val: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/moving_mean"
        string_val: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/moving_variance"
        string_val: "warping_model/warping_module/coarse_level/cnn_blk_0/cnn/kernel"
        string_val: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/beta"
        string_val: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/gamma"
        string_val: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/moving_mean"
        string_val: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/moving_variance"
        string_val: "warping_model/warping_module/coarse_level/cnn_blk_1/cnn/kernel"
        string_val: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/beta"
        string_val: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/gamma"
        string_val: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/moving_mean"
        string_val: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/moving_variance"
        string_val: "warping_model/warping_module/coarse_level/cnn_blk_2/cnn/kernel"
        string_val: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/beta"
        string_val: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/gamma"
        string_val: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/moving_mean"
        string_val: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/moving_variance"
        string_val: "warping_model/warping_module/coarse_level/cnn_blk_3/cnn/kernel"
        string_val: "warping_model/warping_module/fine_level/cnn_4/kernel"
        string_val: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/beta"
        string_val: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/gamma"
        string_val: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/moving_mean"
        string_val: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/moving_variance"
        string_val: "warping_model/warping_module/fine_level/cnn_blk_0/cnn/kernel"
        string_val: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/beta"
        string_val: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/gamma"
        string_val: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/moving_mean"
        string_val: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/moving_variance"
        string_val: "warping_model/warping_module/fine_level/cnn_blk_1/cnn/kernel"
        string_val: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/beta"
        string_val: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/gamma"
        string_val: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/moving_mean"
        string_val: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/moving_variance"
        string_val: "warping_model/warping_module/fine_level/cnn_blk_2/cnn/kernel"
        string_val: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/beta"
        string_val: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/gamma"
        string_val: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/moving_mean"
        string_val: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/moving_variance"
        string_val: "warping_model/warping_module/fine_level/cnn_blk_3/cnn/kernel"
      }
    }
  }
}
node {
  name: "save/RestoreV2/shape_and_slices"
  op: "Const"
  device: "/device:CPU:0"
  attr {
    key: "dtype"
    value {
      type: DT_STRING
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_STRING
        tensor_shape {
          dim {
            size: 59
          }
        }
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
        string_val: ""
      }
    }
  }
}
node {
  name: "save/RestoreV2"
  op: "RestoreV2"
  input: "save/Const"
  input: "save/RestoreV2/tensor_names"
  input: "save/RestoreV2/shape_and_slices"
  device: "/device:CPU:0"
  attr {
    key: "dtypes"
    value {
      list {
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
        type: DT_FLOAT
      }
    }
  }
}
node {
  name: "save/Assign"
  op: "Assign"
  input: "warping_model/encoder/dnn_blk_0/dnn/bias"
  input: "save/RestoreV2"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/encoder/dnn_blk_0/dnn/bias"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_1"
  op: "Assign"
  input: "warping_model/encoder/dnn_blk_0/dnn/kernel"
  input: "save/RestoreV2:1"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/encoder/dnn_blk_0/dnn/kernel"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_2"
  op: "Assign"
  input: "warping_model/encoder/dnn_blk_1/dnn/bias"
  input: "save/RestoreV2:2"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/encoder/dnn_blk_1/dnn/bias"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_3"
  op: "Assign"
  input: "warping_model/encoder/dnn_blk_1/dnn/kernel"
  input: "save/RestoreV2:3"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/encoder/dnn_blk_1/dnn/kernel"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_4"
  op: "Assign"
  input: "warping_model/encoder/dnn_blk_2/dnn/bias"
  input: "save/RestoreV2:4"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/encoder/dnn_blk_2/dnn/bias"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_5"
  op: "Assign"
  input: "warping_model/encoder/dnn_blk_2/dnn/kernel"
  input: "save/RestoreV2:5"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/encoder/dnn_blk_2/dnn/kernel"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_6"
  op: "Assign"
  input: "warping_model/lcm_module/cnn_2/kernel"
  input: "save/RestoreV2:6"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_2/kernel"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_7"
  op: "Assign"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/beta"
  input: "save/RestoreV2:7"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_0/bn_layer/beta"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_8"
  op: "Assign"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/gamma"
  input: "save/RestoreV2:8"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_0/bn_layer/gamma"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_9"
  op: "Assign"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/moving_mean"
  input: "save/RestoreV2:9"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_0/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_10"
  op: "Assign"
  input: "warping_model/lcm_module/cnn_blk_0/bn_layer/moving_variance"
  input: "save/RestoreV2:10"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_0/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_11"
  op: "Assign"
  input: "warping_model/lcm_module/cnn_blk_0/cnn/kernel"
  input: "save/RestoreV2:11"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_0/cnn/kernel"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_12"
  op: "Assign"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/beta"
  input: "save/RestoreV2:12"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_1/bn_layer/beta"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_13"
  op: "Assign"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/gamma"
  input: "save/RestoreV2:13"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_1/bn_layer/gamma"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_14"
  op: "Assign"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/moving_mean"
  input: "save/RestoreV2:14"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_1/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_15"
  op: "Assign"
  input: "warping_model/lcm_module/cnn_blk_1/bn_layer/moving_variance"
  input: "save/RestoreV2:15"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_1/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_16"
  op: "Assign"
  input: "warping_model/lcm_module/cnn_blk_1/cnn/kernel"
  input: "save/RestoreV2:16"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/lcm_module/cnn_blk_1/cnn/kernel"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_17"
  op: "Assign"
  input: "warping_model/warping_module/coarse_level/cnn_4/kernel"
  input: "save/RestoreV2:17"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_4/kernel"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_18"
  op: "Assign"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/beta"
  input: "save/RestoreV2:18"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/beta"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_19"
  op: "Assign"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/gamma"
  input: "save/RestoreV2:19"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/gamma"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_20"
  op: "Assign"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/moving_mean"
  input: "save/RestoreV2:20"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_21"
  op: "Assign"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/moving_variance"
  input: "save/RestoreV2:21"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_0/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_22"
  op: "Assign"
  input: "warping_model/warping_module/coarse_level/cnn_blk_0/cnn/kernel"
  input: "save/RestoreV2:22"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_0/cnn/kernel"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_23"
  op: "Assign"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/beta"
  input: "save/RestoreV2:23"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/beta"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_24"
  op: "Assign"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/gamma"
  input: "save/RestoreV2:24"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/gamma"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_25"
  op: "Assign"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/moving_mean"
  input: "save/RestoreV2:25"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_26"
  op: "Assign"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/moving_variance"
  input: "save/RestoreV2:26"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_1/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_27"
  op: "Assign"
  input: "warping_model/warping_module/coarse_level/cnn_blk_1/cnn/kernel"
  input: "save/RestoreV2:27"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_1/cnn/kernel"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_28"
  op: "Assign"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/beta"
  input: "save/RestoreV2:28"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/beta"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_29"
  op: "Assign"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/gamma"
  input: "save/RestoreV2:29"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/gamma"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_30"
  op: "Assign"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/moving_mean"
  input: "save/RestoreV2:30"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_31"
  op: "Assign"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/moving_variance"
  input: "save/RestoreV2:31"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_2/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_32"
  op: "Assign"
  input: "warping_model/warping_module/coarse_level/cnn_blk_2/cnn/kernel"
  input: "save/RestoreV2:32"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_2/cnn/kernel"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_33"
  op: "Assign"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/beta"
  input: "save/RestoreV2:33"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/beta"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_34"
  op: "Assign"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/gamma"
  input: "save/RestoreV2:34"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/gamma"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_35"
  op: "Assign"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/moving_mean"
  input: "save/RestoreV2:35"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_36"
  op: "Assign"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/moving_variance"
  input: "save/RestoreV2:36"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_3/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_37"
  op: "Assign"
  input: "warping_model/warping_module/coarse_level/cnn_blk_3/cnn/kernel"
  input: "save/RestoreV2:37"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/coarse_level/cnn_blk_3/cnn/kernel"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_38"
  op: "Assign"
  input: "warping_model/warping_module/fine_level/cnn_4/kernel"
  input: "save/RestoreV2:38"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_4/kernel"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_39"
  op: "Assign"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/beta"
  input: "save/RestoreV2:39"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/beta"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_40"
  op: "Assign"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/gamma"
  input: "save/RestoreV2:40"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/gamma"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_41"
  op: "Assign"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/moving_mean"
  input: "save/RestoreV2:41"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_42"
  op: "Assign"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/moving_variance"
  input: "save/RestoreV2:42"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_0/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_43"
  op: "Assign"
  input: "warping_model/warping_module/fine_level/cnn_blk_0/cnn/kernel"
  input: "save/RestoreV2:43"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_0/cnn/kernel"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_44"
  op: "Assign"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/beta"
  input: "save/RestoreV2:44"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/beta"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_45"
  op: "Assign"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/gamma"
  input: "save/RestoreV2:45"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/gamma"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_46"
  op: "Assign"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/moving_mean"
  input: "save/RestoreV2:46"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_47"
  op: "Assign"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/moving_variance"
  input: "save/RestoreV2:47"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_1/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_48"
  op: "Assign"
  input: "warping_model/warping_module/fine_level/cnn_blk_1/cnn/kernel"
  input: "save/RestoreV2:48"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_1/cnn/kernel"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_49"
  op: "Assign"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/beta"
  input: "save/RestoreV2:49"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/beta"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_50"
  op: "Assign"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/gamma"
  input: "save/RestoreV2:50"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/gamma"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_51"
  op: "Assign"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/moving_mean"
  input: "save/RestoreV2:51"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_52"
  op: "Assign"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/moving_variance"
  input: "save/RestoreV2:52"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_2/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_53"
  op: "Assign"
  input: "warping_model/warping_module/fine_level/cnn_blk_2/cnn/kernel"
  input: "save/RestoreV2:53"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_2/cnn/kernel"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_54"
  op: "Assign"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/beta"
  input: "save/RestoreV2:54"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/beta"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_55"
  op: "Assign"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/gamma"
  input: "save/RestoreV2:55"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/gamma"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_56"
  op: "Assign"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/moving_mean"
  input: "save/RestoreV2:56"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/moving_mean"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_57"
  op: "Assign"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/moving_variance"
  input: "save/RestoreV2:57"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_3/bn_layer/moving_variance"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/Assign_58"
  op: "Assign"
  input: "warping_model/warping_module/fine_level/cnn_blk_3/cnn/kernel"
  input: "save/RestoreV2:58"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "_class"
    value {
      list {
        s: "loc:@warping_model/warping_module/fine_level/cnn_blk_3/cnn/kernel"
      }
    }
  }
  attr {
    key: "use_locking"
    value {
      b: true
    }
  }
  attr {
    key: "validate_shape"
    value {
      b: true
    }
  }
}
node {
  name: "save/restore_all"
  op: "NoOp"
  input: "^save/Assign"
  input: "^save/Assign_1"
  input: "^save/Assign_10"
  input: "^save/Assign_11"
  input: "^save/Assign_12"
  input: "^save/Assign_13"
  input: "^save/Assign_14"
  input: "^save/Assign_15"
  input: "^save/Assign_16"
  input: "^save/Assign_17"
  input: "^save/Assign_18"
  input: "^save/Assign_19"
  input: "^save/Assign_2"
  input: "^save/Assign_20"
  input: "^save/Assign_21"
  input: "^save/Assign_22"
  input: "^save/Assign_23"
  input: "^save/Assign_24"
  input: "^save/Assign_25"
  input: "^save/Assign_26"
  input: "^save/Assign_27"
  input: "^save/Assign_28"
  input: "^save/Assign_29"
  input: "^save/Assign_3"
  input: "^save/Assign_30"
  input: "^save/Assign_31"
  input: "^save/Assign_32"
  input: "^save/Assign_33"
  input: "^save/Assign_34"
  input: "^save/Assign_35"
  input: "^save/Assign_36"
  input: "^save/Assign_37"
  input: "^save/Assign_38"
  input: "^save/Assign_39"
  input: "^save/Assign_4"
  input: "^save/Assign_40"
  input: "^save/Assign_41"
  input: "^save/Assign_42"
  input: "^save/Assign_43"
  input: "^save/Assign_44"
  input: "^save/Assign_45"
  input: "^save/Assign_46"
  input: "^save/Assign_47"
  input: "^save/Assign_48"
  input: "^save/Assign_49"
  input: "^save/Assign_5"
  input: "^save/Assign_50"
  input: "^save/Assign_51"
  input: "^save/Assign_52"
  input: "^save/Assign_53"
  input: "^save/Assign_54"
  input: "^save/Assign_55"
  input: "^save/Assign_56"
  input: "^save/Assign_57"
  input: "^save/Assign_58"
  input: "^save/Assign_6"
  input: "^save/Assign_7"
  input: "^save/Assign_8"
  input: "^save/Assign_9"
}
versions {
  producer: 26
}
