#include <primitiv/config.h>

#include <primitiv/cuda_device.h>
#include <primitiv/internal/cuda_utils.h>
#include <primitiv/device_ops/cuda/common.h>

namespace {

__global__ void set_const_dev(float k, std::uint32_t size, float *py) {
  const std::uint32_t i = IDX;
  if (i < size) py[i] = k;
}

}  // namespace

namespace primitiv {
namespace devices {

void CUDA::reset_tensor_impl(float k, Tensor &x) {
  const std::uint32_t size = x.shape().size();
  const std::uint32_t num_blocks = GRID_SIZE(size, dim1_x_);
  CUDA_CALL(::cudaSetDevice(dev_id_));
  ::set_const_dev<<<num_blocks, dim1_x_>>>(k, size, MDATA(x));
}

}  // namespace devices
}  // namespace primitiv
