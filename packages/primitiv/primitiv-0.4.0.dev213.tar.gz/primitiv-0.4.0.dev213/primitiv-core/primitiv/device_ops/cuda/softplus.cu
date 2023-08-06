#include <primitiv/config.h>

#include <primitiv/cuda_device.h>
#include <primitiv/internal/cuda_utils.h>
#include <primitiv/device_ops/cuda/common.h>

namespace {

CUDADEV_KERNEL_FW_X(
    softplus, ::fmaxf(px[i], .0f) + ::logf(1.f + ::expf(-::fabs(px[i]))));
CUDADEV_KERNEL_BW_X(softplus, (.5f + .5f * ::tanhf(.5f * px[i])) * pgy[i]);

}  // namespace

namespace primitiv {
namespace devices {

CUDADEV_FW_X(softplus);
CUDADEV_BW_X(softplus);

}  // namespace devices
}  // namespace primitiv
