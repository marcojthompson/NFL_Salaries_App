// list of team abbreviations
var teamList = ["BUF", "MIA", "NE", "NYJ",
                "BAL", "CIN", "CLE", "PIT",
                "HOU", "IND", "JAX", "TEN",
                "DEN", "KC", "LV", "LAC",
                "DAL", "NYG", "PHI", "WAS",
                "CHI", "DET", "GB", "MIN",
                "ATL", "CAR", "NO", "TB",
                "AZ", "LAR", "SF", "SEA"];
    
// function to populate the dropdown menu
function populateDropdown() {
    var dropdown = document.getElementById("team_choice");

    // First clear the previous options (might be unnecessary)
    dropdown.innerHTML = "";

    // Add options from the data
    for (var i = 0; i < teamList.length; i++) {
        console.log(i)
        var option = document.createElement("option");
        option.value = teamList[i];
        option.text = teamList[i];
        dropdown.appendChild(option);
    }
}

// Call the function to populate the dropdown
populateDropdown()