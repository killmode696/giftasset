# Stars Swap Widget Integration Guide

This guide explains how to integrate the **Stars Swap Widget** into your application using one of the two supported methods:

- [🧩 Native HTML/CSS/JS Integration](#native-integration)
- [⚛️ React Integration](#react-integration)

---

## 🧩 <a name="native-integration"></a>Native HTML/CSS/JS Integration

This method uses plain JavaScript and jQuery to dynamically load and initialize the widget.

### 📥 Load and Initialize the Widget

```js
function loadWidget(callback) {
  var cssUrl = 'https://giftasset.pro/api/v1/stars/src/v1/widget/css/stars-swap.css';
  var jsUrl  = 'https://giftasset.pro/api/v1/stars/src/v1/widget/js/stars-swap-widget.umd.js';

  $('head').append('<link rel="stylesheet" href="' + cssUrl + '" />');

  $.getScript(jsUrl)
    .done(function () {
      initWidget();
      if (callback) callback();
    })
    .fail(function () {
      console.error('Widget init error');
    });
}
```

### ⚙️ Initialize the Widget

```js
function initWidget() {
  if (typeof window.StarsSwapWidget !== 'undefined') {
    window.StarsSwapWidget.init({
      partnerUid: '*your_partner_uid_here*',
    });
  }
}
```

### 🚀 Open the Widget

```js
function openWidget() {
  if (typeof window.StarsSwapWidget !== 'undefined' && window.StarsSwapWidget.open) {
    window.StarsSwapWidget.open({
      tonConnect: window.tonConnectUI
    });
  } else {
    console.error('Widget not loaded');
  }

  document.addEventListener('DOMContentLoaded', function () {
    const widget = document.querySelector('stars-swap-widget');
    if (widget) {
      widget.style.setProperty('z-index', '999', 'important');
    }
  });
}

// Load and open the widget
loadWidget(function () {
  openWidget();
});
```

---

## ⚛️ <a name="react-integration"></a>React Integration (Coming Soon)

> ⚠️ React component-based integration is under development. For now, you can use the native loader inside a `useEffect()` hook as a workaround.

### Example:

```tsx
import { useEffect } from 'react';

export default function StarsWidgetLoader() {
  useEffect(() => {
    const loadWidget = (callback) => {
      const cssUrl = 'https://giftasset.pro/api/v1/stars/src/v1/widget/css/stars-swap.css';
      const jsUrl = 'https://giftasset.pro/api/v1/stars/src/v1/widget/js/stars-swap-widget.umd.js';

      const link = document.createElement('link');
      link.rel = 'stylesheet';
      link.href = cssUrl;
      document.head.appendChild(link);

      const script = document.createElement('script');
      script.src = jsUrl;
      script.onload = () => {
        if (window.StarsSwapWidget) {
          window.StarsSwapWidget.init({
            partnerUid: '*your_partner_uid_here*',
          });
          if (callback) callback();
        }
      };
      document.body.appendChild(script);
    };

    loadWidget(() => {
      if (window.StarsSwapWidget?.open) {
        window.StarsSwapWidget.open({
          tonConnect: window.tonConnectUI,
        });
      }
    });
  }, []);

  return null;
}
```
