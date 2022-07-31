jQuery(document).ready(function () {
  // This button will increment the value
  $('[data-quantity="plus"]').click(function (e) {
    // Stop acting like a button
    e.preventDefault();
    // Get the field name
    fieldName = $(this).attr('data-field');
    // Get its current value
    var currentVal = parseInt($('input[name=' + fieldName + ']').val());
    // If is not undefined
    if (!isNaN(currentVal)) {
      // Increment
      $('input[name=' + fieldName + ']').val(currentVal + 1);
    } else {
      // Otherwise put a 0 there
      $('input[name=' + fieldName + ']').val(0);
    }
  });
  // This button will decrement the value till 0
  $('[data-quantity="minus"]').click(function (e) {
    // Stop acting like a button
    e.preventDefault();
    // Get the field name
    fieldName = $(this).attr('data-field');
    // Get its current value
    var currentVal = parseInt($('input[name=' + fieldName + ']').val());
    // If it isn't undefined or its greater than 0
    if (!isNaN(currentVal) && currentVal > 0) {
      // Decrement one
      $('input[name=' + fieldName + ']').val(currentVal - 1);
    } else {
      // Otherwise put a 0 there
      $('input[name=' + fieldName + ']').val(0);
    }
  });
});


$('[data-addCart]').click(function () {
  $(this).addClass('is-adding')
  setTimeout(function () {
    $('[data-addCart]').removeClass('is-adding')
    $('[data-successMessage]').removeClass('hide')
  }, 2500);
});

$(document).foundation();

$(function () {
  $('.search')
    .bind('click', function (event) {
      $(".search-field").toggleClass("expand-search");

      // if the search field is expanded, focus on it
      if ($(".search-field").hasClass("expand-search")) {
        $(".search-field").focus();
      }
    })
});


