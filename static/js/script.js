$(document).ready(function() {
    // Auto-dismiss the flash message after 1.5 seconds
    setTimeout(function() {
        $(".flash-message").fadeOut('slow');
    }, 1500);

    // Allow the flash message to be closed when the close button is clicked
    $(".flash-message .close").on("click", function() {
        $(this).parent().fadeOut('slow');
    });

    //  credit to https://examples.bootstrap-table.com/#welcome.html
  var $table = $('#table')
  var $remove = $('#remove')
  var selections = []

  function initTable() {
    $table.bootstrapTable('destroy').bootstrapTable({
      height: 1000,
      locale: $('#locale').val(),
    })
    $table.on('check.bs.table uncheck.bs.table ' +
      'check-all.bs.table uncheck-all.bs.table',
    function () {
      $remove.prop('disabled', !$table.bootstrapTable('getSelections').length)

    })

    $remove.click(function () {
      var ids = getIdSelections()
      $table.bootstrapTable('remove', {
        field: 'id',
        values: ids
      })
      $remove.prop('disabled', true)
    })
  }

  $(function() {
    initTable()

    $('#locale').change(initTable)
  })


});
