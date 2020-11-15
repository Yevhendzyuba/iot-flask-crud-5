function checkTypeInputValue() {
    var name = document.forms["myForm"]["name"].value;
    var appoinment = document.forms["myForm"]["appoinment"].value;
    var produce_country = document.forms["myForm"]["produce_country"].value;
    var capacity_in_ml = document.forms["myForm"]["capacity_in_ml"].value;
    var price_in_uah = document.forms["myForm"]["price_in_uah"].value;

    var regex_str = /^[a-zA-Z]+$/;
    var regex_num = /^[0-9]+$/;
    if (!name.match(regex_str) || !appoinment.match(regex_num) || !produce_country.match(regex_str) || !capacity_in_ml.match(regex_num) ||
        !price_in_uah.match(regex_num)
    ) {
        alert("Data entered incorrectly");
    }

}