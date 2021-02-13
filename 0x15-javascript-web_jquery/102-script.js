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
  const myDiv = $('#btn_translate');
  $(myDiv).click(function () {
    const code = $('#language_code').val();
    const queryCode = 'https://www.fourtonfish.com/hellosalut/?lang=' + code;
    console.log(queryCode);
    $.get(queryCode, function (data) {
      $('#hello').html(data.hello);
    });
  });
});
