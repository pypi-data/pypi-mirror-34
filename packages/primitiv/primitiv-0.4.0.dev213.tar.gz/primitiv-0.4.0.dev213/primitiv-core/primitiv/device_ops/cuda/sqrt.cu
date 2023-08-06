#include <primitiv/config.h>

#include <primitiv/cuda_device.h>
#include <primitiv/internal/cuda_utils.h>
#include <primitiv/device_ops/cuda/common.h>

namespace {

CUDADEV_KERNEL_FW_X(sqrt, ::__fsqrt_rn(px[i]));
CUDADEV_KERNEL_BW_X(sqrt, .5f * pgy[i] / py[i]);

}  // namespace

namespace primitiv {
namespace devices {

CUDADEV_FW_X(sqrt);
CUDADEV_BW_X(sqrt);

}  // namespace devices
}  // namespace primitiv
