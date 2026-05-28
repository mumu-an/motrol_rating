# -*- coding: utf-8 -*-
"""浏览器指纹生成工具

用于生成随机的浏览器指纹参数,模拟真实用户环境
"""
import random


# Chrome 142 官方版本号 (2025年10-12月)
# 来源: https://versionhistory.googleapis.com/v1/chrome/platforms/win64/channels/all/versions
CHROME_VERSIONS_WINDOWS = [
    # Stable releases (Desktop: Windows)
    "142.0.7444.243", "142.0.7444.235", "142.0.7444.226",
    "142.0.7444.177", "142.0.7444.176", "142.0.7444.175",
    "142.0.7444.164", "142.0.7444.163", "142.0.7444.162",
    "142.0.7444.136", "142.0.7444.135", "142.0.7444.134",
    "142.0.7444.61", "142.0.7444.60", "142.0.7444.59",
    "142.0.7444.53", "142.0.7444.52",
    # Beta releases
    "142.0.7444.34", "142.0.7444.23", "142.0.7444.6",
    "142.0.7444.3", "142.0.7444.1", "142.0.7444.0",
    # Dev/Canary 版本 (7443.x - 7391.x)
    "142.0.7443.1", "142.0.7443.0", "142.0.7442.2", "142.0.7442.1", "142.0.7442.0",
    "142.0.7441.1", "142.0.7441.0", "142.0.7440.1", "142.0.7440.0",
    "142.0.7439.1", "142.0.7439.0", "142.0.7438.1", "142.0.7438.0",
    "142.0.7437.1", "142.0.7437.0", "142.0.7436.1", "142.0.7436.0",
    "142.0.7435.1", "142.0.7435.0", "142.0.7434.1", "142.0.7434.0",
    "142.0.7433.2", "142.0.7433.0", "142.0.7432.5", "142.0.7432.4",
    "142.0.7432.2", "142.0.7432.0", "142.0.7431.1", "142.0.7431.0",
    "142.0.7430.1", "142.0.7430.0", "142.0.7429.1", "142.0.7429.0",
    "142.0.7428.1", "142.0.7428.0", "142.0.7427.1", "142.0.7427.0",
    "142.0.7426.1", "142.0.7426.0", "142.0.7425.1", "142.0.7425.0",
    "142.0.7424.1", "142.0.7424.0", "142.0.7423.1", "142.0.7423.0",
    "142.0.7422.1", "142.0.7422.0", "142.0.7421.1", "142.0.7421.0",
    "142.0.7420.5", "142.0.7420.4", "142.0.7420.3", "142.0.7420.2",
    "142.0.7420.1", "142.0.7420.0", "142.0.7419.3", "142.0.7419.1",
    "142.0.7419.0", "142.0.7418.4", "142.0.7418.3", "142.0.7418.0",
    "142.0.7417.1", "142.0.7417.0", "142.0.7416.1", "142.0.7416.0",
    "142.0.7415.1", "142.0.7415.0", "142.0.7414.1", "142.0.7414.0",
    "142.0.7413.1", "142.0.7413.0", "142.0.7412.1", "142.0.7412.0",
    "142.0.7411.1", "142.0.7411.0", "142.0.7410.2", "142.0.7410.0",
    "142.0.7409.1", "142.0.7409.0", "142.0.7408.1", "142.0.7408.0",
    "142.0.7407.1", "142.0.7407.0", "142.0.7406.1", "142.0.7406.0",
    "142.0.7405.4", "142.0.7405.3", "142.0.7405.1", "142.0.7405.0",
    "142.0.7404.1", "142.0.7404.0", "142.0.7403.1", "142.0.7403.0",
    "142.0.7402.1", "142.0.7402.0", "142.0.7401.1", "142.0.7401.0",
    "142.0.7400.1", "142.0.7400.0", "142.0.7399.1", "142.0.7399.0",
    "142.0.7398.1", "142.0.7398.0", "142.0.7397.1", "142.0.7397.0",
    "142.0.7396.1", "142.0.7396.0", "142.0.7395.1", "142.0.7395.0",
    "142.0.7394.1", "142.0.7394.0", "142.0.7393.7", "142.0.7393.6",
    "142.0.7393.1", "142.0.7393.0", "142.0.7392.1", "142.0.7392.0",
    "142.0.7391.1", "142.0.7391.0"
]

# 浏览器品牌
BROWSER_BRANDS = ["Chrome", "Edge", "Opera"]

# 内存大小 (GB)
MEMORY_SIZES = [4, 8, 16, 24, 32]

# CPU 核心数
CPU_CORES = [4, 6, 8, 10, 12, 16, 24, 32]

# 屏幕分辨率
SCREEN_RESOLUTIONS = [
    {"width": 1920, "height": 1080},
    {"width": 2560, "height": 1440},
    {"width": 3840, "height": 2160},
    {"width": 3440, "height": 1440},
    {"width": 2560, "height": 1600},
    {"width": 5120, "height": 2880}
]

# Windows 版本信息
WINDOWS_VERSIONS = {
    "10.0": [
        {"nt": "10.0.19041", "code": "Vanadium"},
        {"nt": "10.0.19044", "code": "Iron"},
        {"nt": "10.0.19045", "code": "Vibranium"}
    ],
    "11.0": [
        {"nt": "10.0.22621", "code": "Sun Valley 2"},
        {"nt": "10.0.22631", "code": "Sun Valley 3"}
    ]
}

# GPU Vendor 和 Renderer 配置 (更新于 2025年12月)
# 数据来源: Steam Hardware Survey November 2025, Jon Peddie Research Q3 2025
# 市场份额: NVIDIA 92%, AMD 7%, Intel 1%
# 格式说明:
# - NVIDIA: ANGLE (NVIDIA, {型号} Direct3D11 vs_5_0 ps_5_0) - 不带D3D11后缀
# - AMD: ANGLE (AMD, AMD {型号} Direct3D11 vs_5_0 ps_5_0, D3D11-{驱动版本}) - 带驱动版本
# - Intel: ANGLE (Intel, Intel(R) {型号} Direct3D11 vs_5_0 ps_5_0) - 不带D3D11后缀
GPU_VENDORS_RENDERERS = [
        ("NVIDIA Corporation", [
            # RTX 50 系列 (Blackwell 架构, 2025年1月发布)
            "ANGLE (NVIDIA, NVIDIA GeForce RTX 5090 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE (NVIDIA, NVIDIA GeForce RTX 5080 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE (NVIDIA, NVIDIA GeForce RTX 5070 Ti Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE (NVIDIA, NVIDIA GeForce RTX 5070 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE (NVIDIA, NVIDIA GeForce RTX 5060 Ti Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE (NVIDIA, NVIDIA GeForce RTX 5060 Direct3D11 vs_5_0 ps_5_0)",
            # RTX 40 系列 (Ada Lovelace 架构)
            "ANGLE (NVIDIA, NVIDIA GeForce RTX 4090 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE (NVIDIA, NVIDIA GeForce RTX 4080 SUPER Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE (NVIDIA, NVIDIA GeForce RTX 4080 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE (NVIDIA, NVIDIA GeForce RTX 4070 Ti SUPER Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE (NVIDIA, NVIDIA GeForce RTX 4070 Ti Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE (NVIDIA, NVIDIA GeForce RTX 4070 SUPER Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE (NVIDIA, NVIDIA GeForce RTX 4070 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE (NVIDIA, NVIDIA GeForce RTX 4060 Ti Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE (NVIDIA, NVIDIA GeForce RTX 4060 Direct3D11 vs_5_0 ps_5_0)",
            # RTX 30 系列 (Ampere 架构)
            "ANGLE (NVIDIA, NVIDIA GeForce RTX 3090 Ti Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE (NVIDIA, NVIDIA GeForce RTX 3090 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE (NVIDIA, NVIDIA GeForce RTX 3080 Ti Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE (NVIDIA, NVIDIA GeForce RTX 3080 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE (NVIDIA, NVIDIA GeForce RTX 3070 Ti Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE (NVIDIA, NVIDIA GeForce RTX 3070 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE (NVIDIA, NVIDIA GeForce RTX 3060 Ti Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE (NVIDIA, NVIDIA GeForce RTX 3060 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE (NVIDIA, NVIDIA GeForce RTX 3050 Direct3D11 vs_5_0 ps_5_0)",
            # RTX 20 系列 (Turing 架构)
            "ANGLE (NVIDIA, NVIDIA GeForce RTX 2080 Ti Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE (NVIDIA, NVIDIA GeForce RTX 2080 SUPER Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE (NVIDIA, NVIDIA GeForce RTX 2080 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE (NVIDIA, NVIDIA GeForce RTX 2070 SUPER Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE (NVIDIA, NVIDIA GeForce RTX 2070 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE (NVIDIA, NVIDIA GeForce RTX 2060 SUPER Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE (NVIDIA, NVIDIA GeForce RTX 2060 Direct3D11 vs_5_0 ps_5_0)",
            # GTX 16 系列 (Turing 架构)
            "ANGLE (NVIDIA, NVIDIA GeForce GTX 1660 Ti Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE (NVIDIA, NVIDIA GeForce GTX 1660 SUPER Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE (NVIDIA, NVIDIA GeForce GTX 1660 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE (NVIDIA, NVIDIA GeForce GTX 1650 SUPER Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE (NVIDIA, NVIDIA GeForce GTX 1650 Direct3D11 vs_5_0 ps_5_0)",
            # GTX 10 系列 (Pascal 架构)
            "ANGLE (NVIDIA, NVIDIA GeForce GTX 1080 Ti Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE (NVIDIA, NVIDIA GeForce GTX 1080 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE (NVIDIA, NVIDIA GeForce GTX 1070 Ti Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE (NVIDIA, NVIDIA GeForce GTX 1070 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE (NVIDIA, NVIDIA GeForce GTX 1060 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE (NVIDIA, NVIDIA GeForce GTX 1050 Ti Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE (NVIDIA, NVIDIA GeForce GTX 1050 Direct3D11 vs_5_0 ps_5_0)",
            # GTX 9 系列 (Maxwell 架构)
            "ANGLE (NVIDIA, NVIDIA GeForce GTX 980 Ti Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE (NVIDIA, NVIDIA GeForce GTX 980 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE (NVIDIA, NVIDIA GeForce GTX 970 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE (NVIDIA, NVIDIA GeForce GTX 960 Direct3D11 vs_5_0 ps_5_0)",
            # 入门级
            "ANGLE (NVIDIA, NVIDIA GeForce GT 1030 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE (NVIDIA, NVIDIA GeForce GT 730 Direct3D11 vs_5_0 ps_5_0)"
        ]),
        ("Intel Inc.", [
            # Intel Arc B 系列 (Battlemage, Xe2-HPG 架构, 2024年12月发布)
            "ANGLE (Intel, Intel(R) Arc(TM) B580 Graphics Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE (Intel, Intel(R) Arc(TM) B570 Graphics Direct3D11 vs_5_0 ps_5_0)",
            # Intel Arc A 系列 (Alchemist, Xe-HPG 架构)
            "ANGLE (Intel, Intel(R) Arc(TM) A770 Graphics Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE (Intel, Intel(R) Arc(TM) A750 Graphics Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE (Intel, Intel(R) Arc(TM) A580 Graphics Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE (Intel, Intel(R) Arc(TM) A380 Graphics Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE (Intel, Intel(R) Arc(TM) A310 Graphics Direct3D11 vs_5_0 ps_5_0)",
            # Intel 集成显卡
            "ANGLE (Intel, Intel(R) Iris(R) Xe Graphics Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE (Intel, Intel(R) UHD Graphics 770 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE (Intel, Intel(R) UHD Graphics 750 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE (Intel, Intel(R) UHD Graphics 730 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE (Intel, Intel(R) UHD Graphics 630 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE (Intel, Intel(R) UHD Graphics 620 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE (Intel, Intel(R) HD Graphics 630 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE (Intel, Intel(R) HD Graphics 620 Direct3D11 vs_5_0 ps_5_0)",
            "ANGLE (Intel, Intel(R) HD Graphics 520 Direct3D11 vs_5_0 ps_5_0)"
        ]),
        ("AMD", [
            # RDNA 4 系列 (2025年3月发布, Adrenalin 25.x 驱动)
            "ANGLE (AMD, AMD Radeon RX 9070 XT Direct3D11 vs_5_0 ps_5_0, D3D11-32.0.25001.1001)",
            "ANGLE (AMD, AMD Radeon RX 9070 Direct3D11 vs_5_0 ps_5_0, D3D11-32.0.25001.1001)",
            # RDNA 3 系列 (Adrenalin 24.x 驱动)
            "ANGLE (AMD, AMD Radeon RX 7900 XTX Direct3D11 vs_5_0 ps_5_0, D3D11-31.0.24033.1003)",
            "ANGLE (AMD, AMD Radeon RX 7900 XT Direct3D11 vs_5_0 ps_5_0, D3D11-31.0.24033.1003)",
            "ANGLE (AMD, AMD Radeon RX 7900 GRE Direct3D11 vs_5_0 ps_5_0, D3D11-31.0.24025.1000)",
            "ANGLE (AMD, AMD Radeon RX 7800 XT Direct3D11 vs_5_0 ps_5_0, D3D11-31.0.24033.1003)",
            "ANGLE (AMD, AMD Radeon RX 7700 XT Direct3D11 vs_5_0 ps_5_0, D3D11-31.0.24025.1000)",
            "ANGLE (AMD, AMD Radeon RX 7600 XT Direct3D11 vs_5_0 ps_5_0, D3D11-31.0.24025.1000)",
            "ANGLE (AMD, AMD Radeon RX 7600 Direct3D11 vs_5_0 ps_5_0, D3D11-31.0.24025.1000)",
            # RDNA 2 系列 (Adrenalin 23.x 驱动)
            "ANGLE (AMD, AMD Radeon RX 6950 XT Direct3D11 vs_5_0 ps_5_0, D3D11-31.0.23013.1023)",
            "ANGLE (AMD, AMD Radeon RX 6900 XT Direct3D11 vs_5_0 ps_5_0, D3D11-31.0.23013.1023)",
            "ANGLE (AMD, AMD Radeon RX 6800 XT Direct3D11 vs_5_0 ps_5_0, D3D11-31.0.23013.1023)",
            "ANGLE (AMD, AMD Radeon RX 6800 Direct3D11 vs_5_0 ps_5_0, D3D11-31.0.23013.1023)",
            "ANGLE (AMD, AMD Radeon RX 6750 XT Direct3D11 vs_5_0 ps_5_0, D3D11-31.0.23013.1023)",
            "ANGLE (AMD, AMD Radeon RX 6700 XT Direct3D11 vs_5_0 ps_5_0, D3D11-31.0.23013.1023)",
            "ANGLE (AMD, AMD Radeon RX 6650 XT Direct3D11 vs_5_0 ps_5_0, D3D11-31.0.23013.1023)",
            "ANGLE (AMD, AMD Radeon RX 6600 XT Direct3D11 vs_5_0 ps_5_0, D3D11-31.0.23013.1023)",
            "ANGLE (AMD, AMD Radeon RX 6600 Direct3D11 vs_5_0 ps_5_0, D3D11-31.0.23013.1023)",
            "ANGLE (AMD, AMD Radeon RX 6500 XT Direct3D11 vs_5_0 ps_5_0, D3D11-31.0.23013.1023)",
            # RDNA 1 系列 (Adrenalin 22.x 驱动)
            "ANGLE (AMD, AMD Radeon RX 5700 XT Direct3D11 vs_5_0 ps_5_0, D3D11-30.0.22025.1003)",
            "ANGLE (AMD, AMD Radeon RX 5700 Direct3D11 vs_5_0 ps_5_0, D3D11-30.0.22025.1003)",
            "ANGLE (AMD, AMD Radeon RX 5600 XT Direct3D11 vs_5_0 ps_5_0, D3D11-30.0.22025.1003)",
            "ANGLE (AMD, AMD Radeon RX 5500 XT Direct3D11 vs_5_0 ps_5_0, D3D11-30.0.22025.1003)",
            # Polaris 系列 (Adrenalin 21.x 驱动)
            "ANGLE (AMD, AMD Radeon RX 590 Direct3D11 vs_5_0 ps_5_0, D3D11-27.20.12029.1000)",
            "ANGLE (AMD, AMD Radeon RX 580 Direct3D11 vs_5_0 ps_5_0, D3D11-27.20.12029.1000)",
            "ANGLE (AMD, AMD Radeon RX 570 Direct3D11 vs_5_0 ps_5_0, D3D11-27.20.12029.1000)",
            "ANGLE (AMD, AMD Radeon RX 560 Direct3D11 vs_5_0 ps_5_0, D3D11-27.20.12029.1000)",
            "ANGLE (AMD, AMD Radeon RX 550 Direct3D11 vs_5_0 ps_5_0, D3D11-27.20.12029.1000)"
        ])
    ]


def _generate_device_id():
    """生成随机的 GPU 设备 ID"""
    device_num = random.randint(0, 65535)
    hex_id = format(device_num, '04x')
    return f"(0x0000{hex_id})"

def _randomize_amd_driver_version(gpu_renderer):
    """为 AMD GPU 随机化驱动版本号"""
    import re

    if random.random() < 0.9:
        return re.sub(r', D3D11-[\d.]+\)', ', D3D11)', gpu_renderer)

    if "D3D11-31.0.24033.1003" in gpu_renderer or "D3D11-31.0.24025.1000" in gpu_renderer:
        major = 31
        minor = 0
        build = random.randint(24001, 24121)
        patch = random.randint(1000, 1099)
        new_driver = f"D3D11-{major}.{minor}.{build}.{patch}"
        gpu_renderer = re.sub(r'D3D11-31\.0\.24\d+\.\d+', new_driver, gpu_renderer)

    elif "D3D11-31.0.23013.1023" in gpu_renderer:
        major = 31
        minor = 0
        build = random.randint(23001, 23121)
        patch = random.randint(1000, 1099)
        new_driver = f"D3D11-{major}.{minor}.{build}.{patch}"
        gpu_renderer = re.sub(r'D3D11-31\.0\.23\d+\.\d+', new_driver, gpu_renderer)

    elif "D3D11-30.0.22025.1003" in gpu_renderer:
        major = 30
        minor = 0
        build = random.randint(22001, 22121)
        patch = random.randint(1000, 1099)
        new_driver = f"D3D11-{major}.{minor}.{build}.{patch}"
        gpu_renderer = re.sub(r'D3D11-30\.0\.22\d+\.\d+', new_driver, gpu_renderer)

    elif "D3D11-27.20.12029.1000" in gpu_renderer:
        major = 27
        minor = 20
        build = random.randint(12001, 12121)
        patch = random.randint(1000, 1099)
        new_driver = f"D3D11-{major}.{minor}.{build}.{patch}"
        gpu_renderer = re.sub(r'D3D11-27\.20\.12\d+\.\d+', new_driver, gpu_renderer)

    return gpu_renderer

def _generate_user_agent(os_version, chrome_version, browser_brand="Chrome"):
    """生成 User-Agent"""
    browser_version = chrome_version.split(".")[0] + ".0.0.0"

    ua = f"Mozilla/5.0 (Windows NT {os_version}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{browser_version} Safari/537.36"

    if browser_brand == "Edge":
        ua += f" Edg/{browser_version}"
    elif browser_brand == "Vivaldi":
        ua += " Vivaldi"
    elif browser_brand == "Opera":
        ua += f" OPR/{browser_version}"

    return ua

def _select_gpu_with_market_share():
    """
    根据真实市场份额选择 GPU
    市场份额数据来源: Jon Peddie Research Q3 2025, Steam Hardware Survey November 2025
    - NVIDIA: 92%
    - AMD: 7%
    - Intel: 1%
    """
    vendor_weights = [92, 1, 7]
    vendor_index = random.choices([0, 1, 2], weights=vendor_weights, k=1)[0]

    gpu_vendor, gpu_renderer_list = GPU_VENDORS_RENDERERS[vendor_index]
    gpu_renderer_base = random.choice(gpu_renderer_list)

    return gpu_vendor, gpu_renderer_base

def _select_chrome_version_with_weight():
    """
    版本分布:
    - 稳定版 (7444.243-7444.52): 80%
    - Beta版 (7444.34-7444.0): 15%
    - Dev/Canary版 (7443.x及以下): 5%
    Returns:
        str: Chrome 版本号
    """
    stable_versions = CHROME_VERSIONS_WINDOWS[:17]
    beta_versions = CHROME_VERSIONS_WINDOWS[17:23]
    dev_versions = CHROME_VERSIONS_WINDOWS[23:]

    all_versions = stable_versions + beta_versions + dev_versions
    weights = (
        [80/len(stable_versions)] * len(stable_versions) +
        [15/len(beta_versions)] * len(beta_versions) +
        [5/len(dev_versions)] * len(dev_versions)
    )

    return random.choices(all_versions, weights=weights, k=1)[0]

def _get_hardware_constraints(gpu_renderer):
    """根据 GPU 档次返回合理的硬件配置范围"""
    # 旗舰级: RTX 50系列顶级, RTX 40系列顶级, RX 9070 XT, RX 7900系列
    if any(x in gpu_renderer for x in ["RTX 5090", "RTX 5080", "RTX 4090", "RTX 4080", "RX 9070 XT", "RX 7900 XTX", "RX 7900 XT"]):
        return {
            "cpu_cores": [12, 16, 24, 32],
            "memory": [32, 64],
            "resolutions": [
                {"width": 2560, "height": 1440},
                {"width": 3840, "height": 2160},
                {"width": 3440, "height": 1440},
                {"width": 5120, "height": 2880}
            ]
        }

    # 高端级: RTX 50/40/30系列高端, RX 9070, RX 7800/6900/6800系列
    elif any(x in gpu_renderer for x in ["RTX 5070", "RTX 4070", "RTX 3080", "RTX 3090", "RX 9070", "RX 7800", "RX 6800", "RX 6900"]):
        return {
            "cpu_cores": [8, 10, 12, 16],
            "memory": [16, 32],
            "resolutions": [
                {"width": 1920, "height": 1080},
                {"width": 2560, "height": 1440},
                {"width": 3840, "height": 2160},
                {"width": 3440, "height": 1440}
            ]
        }

    # 中端级: RTX 50/40/30系列中端, RX 7700/7600/6700/6600系列, GTX 16系列
    elif any(x in gpu_renderer for x in ["RTX 5060", "RTX 4060", "RTX 3060", "RTX 3070", "RX 7700", "RX 7600", "RX 6600", "RX 6700", "GTX 1660", "GTX 1650"]):
        return {
            "cpu_cores": [6, 8, 10, 12],
            "memory": [16, 24],
            "resolutions": [
                {"width": 1920, "height": 1080},
                {"width": 2560, "height": 1440},
                {"width": 3440, "height": 1440}
            ]
        }

    # 入门级: GTX 10系列低端, RX 6500/6400/5500系列, Polaris系列
    elif any(x in gpu_renderer for x in ["GTX 1050", "GT 1030", "GT 730", "RX 6400", "RX 6500", "RX 5500", "RX 560", "RX 550", "RX 580", "RX 570"]):
        return {
            "cpu_cores": [4, 6, 8],
            "memory": [8, 16],
            "resolutions": [
                {"width": 1920, "height": 1080},
                {"width": 1600, "height": 900},
                {"width": 1366, "height": 768}
            ]
        }

    # Intel 集成显卡
    elif any(x in gpu_renderer for x in ["UHD", "HD Graphics", "Iris"]):
        return {
            "cpu_cores": [4, 6, 8],
            "memory": [8, 16],
            "resolutions": [
                {"width": 1920, "height": 1080},
                {"width": 1600, "height": 900},
                {"width": 1366, "height": 768}
            ]
        }

    # Intel Arc 独立显卡
    elif any(x in gpu_renderer for x in ["Arc A7", "Arc B5"]):
        return {
            "cpu_cores": [8, 10, 12, 16],
            "memory": [16, 32],
            "resolutions": [
                {"width": 1920, "height": 1080},
                {"width": 2560, "height": 1440}
            ]
        }

    else:
        return {
            "cpu_cores": [6, 8, 10, 12],
            "memory": [8, 16, 24],
            "resolutions": [
                {"width": 1920, "height": 1080},
                {"width": 2560, "height": 1440}
            ]
        }

def generate_random_fingerprint():
    """
    生成随机指纹参数
    Returns:
        dict: 包含以下字段的字典
            - brand: 浏览器品牌
            - brandVersion: (版本号, User-Agent字符串)
            - gpu_vendor: GPU供应商
            - gpu_renderer: GPU渲染器型号 (ANGLE格式)
            - gpuArch: GPU架构
            - hardwareConcurrency: CPU核心数
            - memory: 内存大小 (GB)
            - screen: 屏幕分辨率 {width, height}
            - os: 操作系统类型
            - osVersion: 操作系统版本
            - osInfo: 详细系统信息 {nt, code, platform, os}
            - fingerprint: 指纹种子
    """
    # 1. 选择浏览器品牌
    browser_brand = random.choice(BROWSER_BRANDS)

    # 2. 选择 Chrome 版本 (按权重)
    chrome_version = _select_chrome_version_with_weight()

    # 3. 选择 Windows 版本
    win_version = random.choice(["10.0", "11.0"])
    win_info = random.choice(WINDOWS_VERSIONS[win_version])

    # 4. 生成 User-Agent
    user_agent = _generate_user_agent(win_version, chrome_version, browser_brand)

    # 5. 选择 GPU (按市场份额权重) 并添加设备ID
    gpu_vendor, gpu_renderer_base = _select_gpu_with_market_share()

    # 为AMD显卡生成随机设备ID
    # NVIDIA和Intel不使用设备ID,仅AMD使用
    device_id = _generate_device_id()

    # 根据厂商插入设备ID到正确位置
    if "NVIDIA" in gpu_renderer_base:
        # NVIDIA: 不添加设备ID,保持原格式
        gpu_renderer = gpu_renderer_base
    elif "AMD" in gpu_renderer_base:
        # AMD: 在型号名称后、Direct3D11前插入设备ID,并随机化驱动版本
        gpu_renderer = gpu_renderer_base.replace(" Direct3D11", f" {device_id} Direct3D11")
        gpu_renderer = _randomize_amd_driver_version(gpu_renderer)
    elif "Intel" in gpu_renderer_base:
        # Intel: 不添加设备ID,保持原格式
        gpu_renderer = gpu_renderer_base
    else:
        gpu_renderer = gpu_renderer_base

    # 提取 GPU 架构 (从 renderer 字符串推断)
    # NVIDIA 架构
    if "RTX 50" in gpu_renderer or "RTX 5" in gpu_renderer:
        gpu_arch = "blackwell"
    elif "RTX 40" in gpu_renderer or "RTX 4" in gpu_renderer:
        gpu_arch = "ada lovelace"
    elif "RTX 30" in gpu_renderer or "RTX 3" in gpu_renderer:
        gpu_arch = "ampere"
    elif "RTX 20" in gpu_renderer or "RTX 2" in gpu_renderer:
        gpu_arch = "turing"
    elif "GTX 16" in gpu_renderer:
        # GTX 1660/1650/1630 是 Turing 架构
        gpu_arch = "turing"
    elif "GTX 1" in gpu_renderer:
        # GTX 1080/1070/1060/1050 是 Pascal 架构
        gpu_arch = "pascal"
    elif "GT 1030" in gpu_renderer or "GT 730" in gpu_renderer:
        gpu_arch = "pascal"
    elif "GTX 9" in gpu_renderer:
        gpu_arch = "maxwell"
    # AMD 架构
    elif "RX 90" in gpu_renderer:
        # RX 9070 系列是 RDNA 4 架构
        gpu_arch = "rdna 4"
    elif "RX 79" in gpu_renderer or "RX 78" in gpu_renderer or "RX 77" in gpu_renderer or "RX 76" in gpu_renderer:
        gpu_arch = "rdna 3"
    elif "RX 69" in gpu_renderer or "RX 68" in gpu_renderer or "RX 67" in gpu_renderer or "RX 66" in gpu_renderer or "RX 65" in gpu_renderer:
        gpu_arch = "rdna 2"
    elif "RX 5" in gpu_renderer:
        gpu_arch = "rdna 1"
    elif "RX 5" in gpu_renderer and ("580" in gpu_renderer or "570" in gpu_renderer or "560" in gpu_renderer or "550" in gpu_renderer or "590" in gpu_renderer):
        # RX 580/570/560/550/590 是 Polaris 架构 (GCN 4th Gen)
        gpu_arch = "gcn 4th gen (polaris)"
    # Intel 架构
    elif "UHD" in gpu_renderer or "HD Graphics" in gpu_renderer:
        gpu_arch = "intel integrated"
    elif "Iris" in gpu_renderer:
        gpu_arch = "intel xe"
    elif "Arc B" in gpu_renderer:
        # Arc B系列 (Battlemage) 是 Xe2-HPG 架构
        gpu_arch = "intel xe2-hpg (battlemage)"
    elif "Arc A" in gpu_renderer:
        # Arc A系列 (Alchemist) 是 Xe-HPG 架构
        gpu_arch = "intel xe-hpg (alchemist)"
    elif "Arc" in gpu_renderer:
        # 通用 Arc 显卡
        gpu_arch = "intel xe-hpg"
    else:
        gpu_arch = "unknown"

    # 6. 根据 GPU 档次选择合理的硬件配置
    hw_constraints = _get_hardware_constraints(gpu_renderer)
    hw_concurrency = random.choice(hw_constraints["cpu_cores"])
    memory = random.choice(hw_constraints["memory"])
    screen = random.choice(hw_constraints["resolutions"])

    return {

        "fingerprint": random.randint(100000, 999999999),

        "platform": "windows",
        "platformVersion": win_version,

        # 浏览器品牌和版本 (Chrome 131+)
        "brand": browser_brand,             # --fingerprint-brand=Chrome/Edge/Opera/Vivaldi
        "brandVersion": chrome_version,     # --fingerprint-brand-version=142.0.7444.176

        "hardwareConcurrency": hw_concurrency,

        # GPU 指纹 (Chrome 142+)
        "gpu_vendor": gpu_vendor,           # --fingerprint-gpu-vendor=NVIDIA Corporation
        "gpu_renderer": gpu_renderer,       # --fingerprint-gpu-renderer=ANGLE (...)

        "userAgent": user_agent,

        "memory": memory,
        "screen": screen,

        # GPU 架构 (用于应用层分类,非指纹参数)
        "gpuArch": gpu_arch,

        # 详细系统信息 (用于应用层,非指纹参数)
        "osInfo": {
            "nt": win_info["nt"],
            "code": win_info["code"],
            "platform": "Win32",
            "os": "Windows"
        }
    }
