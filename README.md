<picture>
  <source media="(prefers-color-scheme: light)" srcset="./assets/banner-light.svg">
  <img alt="Yuri Neves · Firmware & software · Marine Telematics. Frame CAN 2.0A com ID 0x2A5 e dados 'hello' decodificado." src="./assets/banner-dark.svg" width="100%">
</picture>

<p>
  <a href="https://github.com/yuri-ncs"><img alt="GitHub @yuri-ncs" src="https://img.shields.io/badge/%40yuri--ncs-1F6FD6?style=for-the-badge&logo=github&logoColor=white"></a>
  <a href="mailto:yurineves2204@gmail.com"><img alt="E-mail yurineves2204@gmail.com" src="https://img.shields.io/badge/yurineves2204%40gmail.com-0B1A33?style=for-the-badge&logo=gmail&logoColor=8AC0FF"></a>
  <a href="https://github.com/Marine-Telematics"><img alt="Marine Telematics no GitHub" src="https://img.shields.io/badge/%40Marine--Telematics-0B1A33?style=for-the-badge&logo=github&logoColor=8AC0FF"></a>
</p>

## `0x01` Sobre mim

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
        .foco   = "ECUs de propulsão e telemetria marítima",
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

## `0x02` Stack

<table>
  <tr>
    <td><code>linguagens</code></td>
    <td>
      <img alt="C++" src="https://img.shields.io/badge/C%2B%2B-0B1A33?style=flat-square&logo=cplusplus&logoColor=8AC0FF">
      <img alt="C" src="https://img.shields.io/badge/C-0B1A33?style=flat-square&logo=c&logoColor=8AC0FF">
      <img alt="Rust" src="https://img.shields.io/badge/Rust-0B1A33?style=flat-square&logo=rust&logoColor=8AC0FF">
      <img alt="Python" src="https://img.shields.io/badge/Python-0B1A33?style=flat-square&logo=python&logoColor=8AC0FF">
      <img alt="Dart" src="https://img.shields.io/badge/Dart-0B1A33?style=flat-square&logo=dart&logoColor=8AC0FF">
      <img alt="C#" src="https://img.shields.io/badge/C%23-0B1A33?style=flat-square&logo=dotnet&logoColor=8AC0FF">
    </td>
  </tr>
  <tr>
    <td><code>embarcado</code></td>
    <td>
      <img alt="ESP-IDF" src="https://img.shields.io/badge/ESP--IDF-0B1A33?style=flat-square&logo=espressif&logoColor=8AC0FF">
      <img alt="STM32 HAL" src="https://img.shields.io/badge/STM32%20HAL-0B1A33?style=flat-square&logo=stmicroelectronics&logoColor=8AC0FF">
      <img alt="Embassy" src="https://img.shields.io/badge/Embassy-0B1A33?style=flat-square&logo=rust&logoColor=8AC0FF">
      <img alt="FreeRTOS" src="https://img.shields.io/badge/FreeRTOS-0B1A33?style=flat-square">
      <img alt="LVGL" src="https://img.shields.io/badge/LVGL-0B1A33?style=flat-square">
    </td>
  </tr>
  <tr>
    <td><code>aplicações</code></td>
    <td>
      <img alt="Flutter" src="https://img.shields.io/badge/Flutter-0B1A33?style=flat-square&logo=flutter&logoColor=8AC0FF">
      <img alt=".NET Avalonia" src="https://img.shields.io/badge/.NET%20%C2%B7%20Avalonia-0B1A33?style=flat-square&logo=dotnet&logoColor=8AC0FF">
      <img alt="Dear ImGui" src="https://img.shields.io/badge/Dear%20ImGui-0B1A33?style=flat-square">
      <img alt="Electron" src="https://img.shields.io/badge/Electron-0B1A33?style=flat-square&logo=electron&logoColor=8AC0FF">
    </td>
  </tr>
  <tr>
    <td><code>ferramentas</code></td>
    <td>
      <img alt="BUSMASTER" src="https://img.shields.io/badge/BUSMASTER-0B1A33?style=flat-square">
      <img alt="J-Link" src="https://img.shields.io/badge/J--Link-0B1A33?style=flat-square">
      <img alt="Kvaser, PEAK, SocketCAN" src="https://img.shields.io/badge/Kvaser%20%C2%B7%20PEAK%20%C2%B7%20SocketCAN-0B1A33?style=flat-square">
      <img alt="KiCad" src="https://img.shields.io/badge/KiCad-0B1A33?style=flat-square&logo=kicad&logoColor=8AC0FF">
      <img alt="Claude Code" src="https://img.shields.io/badge/Claude%20Code-0B1A33?style=flat-square&logo=claude&logoColor=8AC0FF">
    </td>
  </tr>
  <tr>
    <td><code>qualidade</code></td>
    <td>
      <img alt="gtest" src="https://img.shields.io/badge/gtest-0B1A33?style=flat-square&logo=google&logoColor=8AC0FF">
      <img alt="pytest" src="https://img.shields.io/badge/pytest-0B1A33?style=flat-square&logo=pytest&logoColor=8AC0FF">
      <img alt="HIL" src="https://img.shields.io/badge/HIL-0B1A33?style=flat-square">
      <img alt="GitHub Actions" src="https://img.shields.io/badge/GitHub%20Actions-0B1A33?style=flat-square&logo=githubactions&logoColor=8AC0FF">
      <img alt="Docker" src="https://img.shields.io/badge/Docker-0B1A33?style=flat-square&logo=docker&logoColor=8AC0FF">
    </td>
  </tr>
</table>

## `0x03` Atividade

<p>
  <img height="165" alt="Estatísticas do GitHub de yuri-ncs" src="https://github-readme-stats.vercel.app/api?username=yuri-ncs&show_icons=true&hide_border=true&border_radius=12&bg_color=0B1A33&title_color=8AC0FF&text_color=CFDAEA&icon_color=1F6FD6&locale=pt-br">
  <img height="165" alt="Linguagens mais usadas por yuri-ncs" src="https://github-readme-stats.vercel.app/api/top-langs/?username=yuri-ncs&layout=compact&hide_border=true&border_radius=12&bg_color=0B1A33&title_color=8AC0FF&text_color=CFDAEA&locale=pt-br">
</p>

---

<sub><code>~/yuri-ncs $ exit</code> &nbsp;·&nbsp; <b>ACK</b> · Valeu pela visita</sub>
