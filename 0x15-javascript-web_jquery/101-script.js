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
  // DOM is loaded and ready for manipulation here
  const myDivAdd = $('#add_item');
  $(myDivAdd).click(function () {
    $('.my_list').append('<li>Item</li>');
  });

  const myDivRemove = $('#remove_item');
  $(myDivRemove).click(function () {
    $('li').last().remove();
    console.log('hole');
  });

  const myDivClear = $('#clear_list');
  $(myDivClear).click(function () {
    $('.my_list').empty();
    console.log('holi');
  });
});
