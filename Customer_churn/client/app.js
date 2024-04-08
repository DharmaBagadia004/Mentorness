function getRadioValue(name) {
  var radios = document.getElementsByName(name);
  for (var i = 0; i < radios.length; i++) {
    if (radios[i].checked) {
      return parseInt(radios[i].value);
    }
  }
  return -1; // Invalid Value
}

function getTextValue(id) {
  var element = document.getElementById(id);
  return parseFloat(element.value);
}

function getDropdownValue(id) {
  var element = document.getElementById(id);
  return element.value;
}

function onClickedCustomerChurn() {
  console.log("Customer Churn Button Clicked");

  var gender = getDropdownValue("uigender");
  var seniorcitizen = getRadioValue("uiSenior");
  var partner = getRadioValue("uipartner");
  var dependents = getRadioValue("uidependents");
  var tenure = getRadioValue("uitenure");
  var phoneservice = getRadioValue("uiphoneservice");
  var multiplelines = getRadioValue("uimultiplelines");
  var onlinesecurity = getRadioValue("uionlinesecurity");
  var onlinebackup = getRadioValue("uionlinebackup");
  var deviceprotection = getRadioValue("uideviceprotection");
  var techsupport = getRadioValue("uitechsupport");
  var streamingtv = getRadioValue("uistreamingtv");
  var streamingmovies = getRadioValue("uistreamingmovies");
  var paperlessbilling = getRadioValue("uipaperlessbilling");
  var monthlycharges = getTextValue("uimonthlycharges");
  var totalcharges = getTextValue("uitotalcharges");
  var internetservice = getDropdownValue("uiinternetservice");
  var contract = getDropdownValue("uicontract");
  var paymentmethod = getDropdownValue("uipaymentmethod");

  var url = "http://127.0.0.1:5000/predict_customer_churn";

  $.post(
    url,
    {
      gender: gender,
      seniorcitizen: seniorcitizen,
      partner: partner,
      dependents: dependents,
      tenure: tenure,
      phoneservice: phoneservice,
      multiplelines: multiplelines,
      onlinesecurity: onlinesecurity,
      onlinebackup: onlinebackup,
      deviceprotection: deviceprotection,
      techsupport: techsupport,
      streamingtv: streamingtv,
      streamingmovies: streamingmovies,
      paperlessbilling: paperlessbilling,
      monthlycharges: monthlycharges,
      totalcharges: totalcharges,
      internetservice: internetservice,
      paymentmethod: paymentmethod,
      contract: contract,
    },
    function (data, status) {
      var estPrice = document.getElementById("uiEstimatedPrice");
      if (data.estimated_churn == 0) {
        estPrice.innerHTML = "<h2>NO</h2>";
      } else {
        estPrice.innerHTML = "<h2>YES</h2>";
      }
      console.log(status);
    }
  );
}

function onPageLoad() {
  console.log("document loaded");
  loadDropdownOptions(
    "uipaymentmethod",
    "http://127.0.0.1:5000/get_paymentmethod_types"
  );
  loadDropdownOptions("uicontract", "http://127.0.0.1:5000/get_contract_types");
  loadDropdownOptions(
    "uiinternetservice",
    "http://127.0.0.1:5000/get_internetservice_types"
  );
}

function loadDropdownOptions(elementId, url) {
  $.get(url, function (data, status) {
    if (data) {
      var options = data[elementId];
      var dropdown = document.getElementById(elementId);
      $(dropdown).empty();
      options.forEach(function (option) {
        var opt = new Option(option);
        $(dropdown).append(opt);
      });
    }
  });
}

window.onload = onPageLoad;
