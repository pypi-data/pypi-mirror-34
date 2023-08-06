#include <primitiv/config.h>

#include <cmath>

#include <primitiv/naive_device.h>
#include <primitiv/device_ops/naive/common.h>

namespace primitiv {
namespace devices {

CPUDEV_FW_X(cos, std::cos(src[i]));
CPUDEV_BW_X(cos, -std::sin(px[i]) * pgy[i]);

}  // namespace devices
}  // namespace primitiv
