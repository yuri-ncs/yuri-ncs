<picture>
  <source media="(prefers-color-scheme: light)" srcset="./assets/banner-light.svg">
  <img alt="Yuri Neves · Firmware & software · Marine Telematics · propulsão, telemetria e automação marítima. Frame CAN 2.0A com ID 0x2A5 e dados 'hello' decodificado." src="./assets/banner-dark.svg" width="100%">
</picture>

<p>
  <a href="https://github.com/yuri-ncs"><img alt="GitHub @yuri-ncs" src="https://img.shields.io/badge/%40yuri--ncs-1F6FD6?style=for-the-badge&logo=github&logoColor=white"></a>
  <a href="mailto:yurineves2204@gmail.com"><img alt="E-mail yurineves2204@gmail.com" src="https://img.shields.io/badge/yurineves2204%40gmail.com-0B1A33?style=for-the-badge&logo=gmail&logoColor=8AC0FF"></a>
  <a href="https://github.com/Marine-Telematics"><img alt="Marine Telematics no GitHub" src="https://img.shields.io/badge/%40Marine--Telematics-0B1A33?style=for-the-badge&logo=github&logoColor=8AC0FF"></a>
</p>

<picture>
  <source media="(prefers-color-scheme: light)" srcset="./assets/h-sobre-light.svg">
  <img alt="0x01 Sobre mim" src="./assets/h-sobre-dark.svg" width="100%">
</picture>

<details open>
<summary><b>yuri.h</b></summary>

```cpp
#ifndef YURI_H
#define YURI_H

#include "marine_telematics.h"

// Firmware & software · Marine Telematics · desde 2024
class Yuri {
public:
    struct Cargo {
        const char* titulo;
        const char* foco;
    };

    static constexpr Cargo cargo = {
        .titulo = "Firmware & Software Developer",
        .foco   = "propulsão, telemetria e automação marítima",
    };

    static constexpr Mcu mcus[] = {
        Mcu::ESP32,
        Mcu::STM32,
        Mcu::MSPM0,
    };

    static constexpr Bus barramentos[] = {
        Bus::CAN,      // j1939 | nmea2000 | iso11783
        Bus::RS485,    // j1708 | j1587
        Bus::SERIAL,   // uart | rs232
        Bus::I2C,
        Bus::SPI,
        Bus::USB,      // vendor class | winusb | libusb
    };

    static constexpr Radio radio[] = {
        Radio::BLE,    // gatt | ota
        Radio::WIFI,   // softap | esp-now
        Radio::LTE_4G,
        Radio::LORA,
    };

    static constexpr Tool kit[] = {
        Tool::BUSMASTER,
        Tool::J_LINK,
        Tool::CLAUDE_CODE,
    };

    static constexpr const char* por_fora[] = {
        "Rust embarcado",
        "Go",
    };

    [[noreturn]] void work();
};

#endif // YURI_H
```

</details>

<picture>
  <source media="(prefers-color-scheme: light)" srcset="./assets/h-stack-light.svg">
  <img alt="0x02 Stack" src="./assets/h-stack-dark.svg" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: light)" srcset="./assets/stack-light.svg">
  <img alt="Stack. Linguagens: C++, C, Rust, Python, Dart, C#. Embarcado: ESP-IDF, STM32 HAL, Embassy, FreeRTOS, LVGL. Aplicações: Flutter, .NET Avalonia, Dear ImGui, Electron. Ferramentas: BUSMASTER, J-Link, Kvaser, PEAK, SocketCAN, KiCad, Claude Code. Qualidade: gtest, pytest, HIL, GitHub Actions, Docker." src="./assets/stack-dark.svg" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: light)" srcset="./assets/h-atividade-light.svg">
  <img alt="0x03 Atividade" src="./assets/h-atividade-dark.svg" width="100%">
</picture>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: light)" srcset="https://streak-stats.demolab.com/?user=yuri-ncs&locale=pt_BR&hide_border=true&border_radius=16&card_width=1000&card_height=200&disable_animations=true&background=F6F8FC&stroke=DCE5F2&ring=1F6FD6&fire=1F6FD6&currStreakNum=0B1A33&sideNums=0B1A33&currStreakLabel=1F6FD6&sideLabels=475A78&dates=64748B">
    <img alt="Contribuições e sequência de dias com commits de yuri-ncs" src="https://streak-stats.demolab.com/?user=yuri-ncs&locale=pt_BR&hide_border=true&border_radius=16&card_width=1000&card_height=200&disable_animations=true&background=081226&stroke=1E3358&ring=1F6FD6&fire=8AC0FF&currStreakNum=FFFFFF&sideNums=FFFFFF&currStreakLabel=8AC0FF&sideLabels=B4C3D9&dates=5C7399" width="100%">
  </picture>
</p>

<picture>
  <source media="(prefers-color-scheme: light)" srcset="./assets/footer-light.svg">
  <img alt="~/yuri-ncs $ exit · ACK · valeu pela visita" src="./assets/footer-dark.svg" width="100%">
</picture>
