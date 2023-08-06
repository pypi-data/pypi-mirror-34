#include <primitiv/config.h>

#include <primitiv/cuda16_device.h>
#include <primitiv/internal/cuda_utils.h>
#include <primitiv/device_ops/cuda16/common.h>

namespace {

__global__ void fp32to16(const float *px, std::size_t size, half *py) {
  const std::size_t i = IDX;
  if (i < size) py[i] = ::__float2half(px[i]);
}

}  // namespace

namespace primitiv {
namespace devices {

void CUDA16::random_normal_impl(float mean, float sd, Tensor &y) {
  const std::size_t size = y.shape().size();
  const std::size_t gs = GRID_SIZE(size, dim1_x_);
  auto temp = state_->pool.allocate(size * sizeof(float));
  float *temp_ptr = static_cast<float *>(temp.get());

  CUDA_CALL(::cudaSetDevice(dev_id_));
  CURAND_CALL(::curandGenerateNormal(
        state_->curand.get(), temp_ptr, size, mean, sd));
  ::fp32to16<<<gs, dim1_x_>>>(temp_ptr, size, MDATA(half, y));
}

}  // namespace devices
}  // namespace primitiv
