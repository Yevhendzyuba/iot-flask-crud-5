var x = document.getElementById("first_card_price_in_uah").innerHTML;
var y = document.getElementById("second_card_price_in_uah").innerHTML;
var z = document.getElementById("third_card_price_in_uah").innerHTML;
var k = document.getElementById("four_card_price_in_uah").innerHTML;
var arrayPrice = [x, y, z, k]

function priceCounter(arr) {
    var sum = 0;
    for (var i = 0; i < arrayPrice.length; i++) {
        sum += parseInt(arrayPrice[i]);
    }
    document.getElementById("count").innerHTML = sum;

}

function searchFunction() {
    let input, filter, myCards, card, produce_country, i, txtValue;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    myCards = document.getElementById("myCards");
    card = myCards.getElementsByClassName("card");
    for (i = 0; i < card.length; i++) {
        produce_country = card[i].getElementsByClassName("produce_country")[0];
        txtValue = produce_country.textContent || produce_country.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            card[i].style.display = "";
        } else {
            card[i].style.display = "none";
        }
    }
}

function sortFunction(parent, childSelector, keySelector) {
    var items = parent.children(childSelector).sort(function(a, b) {
        var vA = $(keySelector, a).text();
        var vB = $(keySelector, b).text();
        vA = parseFloat(vA)
        vB = parseFloat(vB)
        return (vA > vB) ? -1 : (vA < vB) ? 1 : 0;
    });
    parent.append(items);
}

$('#sScale').data("sortKey", "span.capacity_in_ml");

$(document).ready(function() {
    $('input[type="checkbox"]').click(function() {
        if ($(this).prop("checked") === true) {
            sortFunction($('.row'), "div", $(this).data("sortKey"));

        }
    });
});