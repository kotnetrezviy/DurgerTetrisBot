let tg = Telegram.WebApp;
tg.expand();

function setThemeClass() {
    document.documentElement.className = Telegram.WebApp.colorScheme;
}

Telegram.WebApp.onEvent('themeChanged', setThemeClass);
setThemeClass();