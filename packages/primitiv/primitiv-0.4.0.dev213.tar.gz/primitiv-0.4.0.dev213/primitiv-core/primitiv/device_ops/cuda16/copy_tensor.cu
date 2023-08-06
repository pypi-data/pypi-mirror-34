#include <primitiv/config.h>

#include <primitiv/cuda16_device.h>
#include <primitiv/internal/cuda_utils.h>
#include <primitiv/device_ops/cuda16/common.h>

namespace primitiv {
namespace devices {

void CUDA16::copy_tensor_impl(const Tensor &x, Tensor &y) {
  switch (x.device().type()) {
    case Device::DeviceType::NAIVE:
      reset_tensor_by_array(CDATA(float, x), y);
      break;
    //case Device::DeviceType::CUDA:
      // TODO(odashi): Implement this section.
    case Device::DeviceType::CUDA16:
      CUDA_CALL(::cudaSetDevice(dev_id_));
      // NOTE(odashi):
      // If source/destination devices use the unified memory space on the 64
      // bits machine, we can perform ::cudaMemcpy to copy data beyond devices.
      CUDA_CALL(::cudaMemcpyAsync(
            MDATA(half, y), CDATA(half, x),
            sizeof(half) * x.shape().size(),
            cudaMemcpyDeviceToDevice, 0));
      break;
    default:
      reset_tensor_by_vector(x.to_vector(), y);
  }
}

}  // namespace devices
}  // namespace primitiv
