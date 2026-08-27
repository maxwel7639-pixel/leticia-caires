// So um pouco de esmalte: fechar as outras perguntas do FAQ quando uma abre.
document.addEventListener('DOMContentLoaded', function () {
  var itens = document.querySelectorAll('.item-faq');
  itens.forEach(function (item) {
    item.addEventListener('toggle', function () {
      if (item.open) {
        itens.forEach(function (outro) {
          if (outro !== item) outro.open = false;
        });
      }
    });
  });
});
