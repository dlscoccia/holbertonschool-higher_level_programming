function docReady (fn) {
  // see if DOM is already available
  if (document.readyState === 'complete' || document.readyState === 'interactive') {
    // call on next available tick
    setTimeout(fn, 1);
  } else {
    document.addEventListener('DOMContentLoaded', fn);
  }
}

docReady(function () {
  function translateHello () {
    const code = $('#language_code').val();
    const queryCode = 'https://www.fourtonfish.com/hellosalut/?lang=' + code;
    console.log(queryCode);
    $.get(queryCode, function (data) {
      $('#hello').html(data.hello);
    });
  }

  $('#language_code').keypress(function (event) {
    const keycode = (event.keyCode ? event.keyCode : event.which);
    if (keycode == '13') {
      translateHello();
    }
  });

  const myDiv = $('#btn_translate');
  $(myDiv).click(function () {
    translateHello();
  });
});
