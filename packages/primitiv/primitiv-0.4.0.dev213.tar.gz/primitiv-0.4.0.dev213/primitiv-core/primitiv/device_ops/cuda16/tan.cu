#include <primitiv/config.h>

#include <primitiv/cuda16_device.h>
#include <primitiv/internal/cuda_utils.h>
#include <primitiv/device_ops/cuda16/common.h>

namespace {

CUDA16_KERNEL_FW_X(tan, ::tanf(X_VAL));
CUDA16_KERNEL_BW_X(tan, (1.f + Y_VAL * Y_VAL) * GY_VAL);

}  // namespace

namespace primitiv {
namespace devices {

CUDA16_DEV_FW_X(tan);
CUDA16_DEV_BW_X(tan);

}  // namespace devices
}  // namespace primitiv
