**WIDGET INTEGRATION**
- native html/css/js loader

# NATIVE HTML/CSS/JS LOADER

```html
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
          console.error('widget init error');
      });
}

function initWidget() {
    if (typeof window.StarsSwapWidget !== 'undefined') {
        window.StarsSwapWidget.init({
            partnerUid: '*your_partner_uid_here*',
        });
    }
}

function openWidget() {
    if (typeof window.StarsSwapWidget !== 'undefined' && window.StarsSwapWidget.open) {
        window.StarsSwapWidget.open({
            tonConnect: window.tonConnectUI
        });
    } else {
        console.error('widget not loaded');
    }

    document.addEventListener('DOMContentLoaded', function() {
    const widget = document.querySelector('stars-swap-widget');
    if (widget) {
        widget.style.setProperty('z-index', '999', 'important');
    }
    });
}


loadWidget(function() {
  openWidget();
});
```
