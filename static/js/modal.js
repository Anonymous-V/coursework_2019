(function($) {
  var dialog;
  $('.trigger').on('click', function() {
    dialog = $('#' + $(this).data('dialog'));
    $(dialog).addClass('dialog--open');
  });
  $('.action, .dialog__overlay').on('click', function() {
    $(dialog).removeClass('dialog--open');
    $(dialog).addClass('dialog--close');
    $(dialog).find('.dialog__content').on('webkitAnimationEnd MSAnimationEnd oAnimationEnd animationend', function() {
      $(dialog).removeClass('dialog--close');
    });
  });

  // $('.dialogEffects').on('click', function(e) {
  //   e.preventDefault();
  //   $('.dialogEffects').removeClass('selected');
  //   $(this).addClass('selected');
  //   var cssClass = $(this).data('class');
  //   $('#dialogEffects').removeAttr('class').addClass(cssClass);
  // });
})(jQuery);