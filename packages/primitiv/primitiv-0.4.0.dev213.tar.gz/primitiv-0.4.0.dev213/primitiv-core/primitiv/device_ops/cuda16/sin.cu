#include <primitiv/config.h>

#include <primitiv/cuda16_device.h>
#include <primitiv/internal/cuda_utils.h>
#include <primitiv/device_ops/cuda16/common.h>

namespace {

CUDA16_KERNEL_FW_X(sin, ::sinf(X_VAL));
CUDA16_KERNEL_BW_X(sin, ::cosf(X_VAL) * GY_VAL);

}  // namespace

namespace primitiv {
namespace devices {

CUDA16_DEV_FW_X(sin);
CUDA16_DEV_BW_X(sin);

}  // namespace devices
}  // namespace primitiv
