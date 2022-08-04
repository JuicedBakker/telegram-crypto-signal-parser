# Cryptocurrency Signal Parser

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

This parsing algorithm allows you to parse so called "cryptocurrency signals". These signals are commonly found in telegram groups and are formatted based on their source. However, it would be way more organized if all these signals would share the same format. Well, that's exactly what this program does. It can be used just to monitor trades more easily, but is best when it is combined with an autotrading algorithm you already own.

<!-- ROADMAP -->
## Roadmap

- [x] Parse symbols / (entry, target, stop loss)
- [ ] Write more in depth documentation.
- [ ] Add Telegram / discord integration
- [ ] Adding a frontend/UI for easier usage
- [ ] Add Binance integration for automated trading.

See the [open issues](https://github.com/JuicedBakker/crypto-signal-parser/issues) for a full list of proposed features (and known issues).

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## The goal of this project

I'm aiming towards making an app which is used by the client, which everyone can use to automatically open trades that are posted in telegram groups. So even if you're busy that day, you can still follow the trades posted in the channels you follow. I believe this would enable people to trade more efficiently and allow them to not be on their phone, worrying about missing anything.

## Usage

1. Clone this repository.
2. Install the necessary requirements.
3. Update the `API_ID`, `API_HASH` and `APP_NAME` in config/config.yml. For API key and id go to https://my.telegram.org/apps
4. Run the app using python3 main.py
5. Enable/disable channels using the menu
6. Start listening to signals using the second menu option.

## Examples

### Original signal
```
CTK  / USDT

LONG  : 1.38

Leverage X10 X25

Target :

TARGET 1  : 1.43$
TARGET 2  : 1.49$
TARGET 3  : 1.53$
TARGET 4  : 1.58$

STOP : 1.28$
```

### Parsed signal
```json
{
    "symbol": "CTKUSDT",
    "entry": [
        1.38
    ],
    "targets": [
        1.43,
        1.49,
        1.53,
        1.58
    ],
    "stop_loss": [
        1.28
    ]
}
```

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/JuicedBakker/crypto-signal-parser?style=for-the-badge
[contributors-url]: https://github.com/JuicedBakker/crypto-signal-parser/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/JuicedBakker/crypto-signal-parser?style=for-the-badge
[forks-url]: https://github.com/JuicedBakker/crypto-signal-parser/network/members
[stars-shield]: https://img.shields.io/github/stars/JuicedBakker/crypto-signal-parser?style=for-the-badge
[stars-url]: https://github.com/JuicedBakker/crypto-signal-parser/stargazers
[issues-shield]: https://img.shields.io/github/issues/JuicedBakker/crypto-signal-parser?style=for-the-badge
[issues-url]: https://github.com/JuicedBakker/crypto-signal-parser/issues
[license-shield]: https://img.shields.io/github/JuicedBakker/crypto-signal-parser?style=for-the-badge
[license-url]: https://github.com/JuicedBakker/crypto-signal-parser/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/joostmbakker/

