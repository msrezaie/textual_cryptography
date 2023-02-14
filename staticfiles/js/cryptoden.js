var cipherSelect = document.getElementById("cipher-select");

// attaching the cipher key div name to the cipher name is a must 
var cipherKeyMap = {
    "Caesar": "key-caesar",
    "Atbash": "key-none",
    "Affine": "key-affine",
};

function selectedCipherKeyInputFields() {
    var selectedCipher = cipherSelect.value;
    var selectedCipherKeyDiv = cipherKeyMap[selectedCipher];
    var selectedCipherKeyinputId = document.getElementById(selectedCipherKeyDiv);
    var keyInputs = selectedCipherKeyinputId.querySelectorAll("input");
    
    return keyInputs;
}

function updateCiphers() {
    var operationId = document.getElementById("operation-select").value;
    // 'opertaions' is taken from index.html
    var loadedCiphers = ciphers[operationId];

    cipherSelect.innerHTML = "";
    
    if (loadedCiphers) {
        for (var i = 0; i < loadedCiphers.length; i++) {
            if (loadedCiphers[i] in cipherKeyMap) {
                cipherSelect.innerHTML += "<option value='" + loadedCiphers[i] + "'>" + loadedCiphers[i] + "</option>";
            } else {
                cipherSelect.innerHTML += "<option disabled value='" + loadedCiphers[i] + "'>" + loadedCiphers[i] + "</option>";
            }
        }
    } else {
        cipherSelect.innerHTML = "<option value=''>Select Operation First</option>";
    }
}

function updateOperationDescription() {
    var operationId = document.getElementById("operation-select").value;
    // 'operationDesc' is taken from index.html
    var operationDesc = document.getElementById("operation-desc");
    var desc = operationDescs[operationId];

    operationDesc.innerHTML = desc;
}

function updateCipherDescription() {
    var cipherName = document.getElementById("cipher-select").value;
    var cipherDesc = document.getElementById("cipher-desc");
    var desc = cipherDescs[cipherName];
    
    cipherDesc.innerHTML = desc;
}

function updateCipherKey() {
    var selectedCipher = cipherSelect.value;
    var selectedCipherKeyDiv = cipherKeyMap[selectedCipher];
    var keyInputDiv = document.querySelectorAll(".keys div");
    var keyInputs = selectedCipherKeyInputFields();
    checkInput();
    for (var i = 0; i < keyInputDiv.length; i++) {
        keyInputDiv[i].style.display = "none";
    }
    for (var i = 0; i < keyInputs.length; i++) {
        keyInputs[i].value = "";
    }
    document.getElementById(selectedCipherKeyDiv).style.display = "block";
}

function caesarValidateInput(input) {
    if (input.value > 25) {
        input.value = 25;
    }
}

function affineValidateInput(input) {
    //
}

function checkInput() {
    var keyInputs = selectedCipherKeyInputFields();
    var plainTextarea = document.getElementById("plainTextarea");

    // get the encrypt button
    const encryptBtn = document.getElementById("encryptBtn");
    function checkEncryptInput() {
        for (var i = 0; i < keyInputs.length; i++) {
            if (keyInputs[i].id == "null") {
                if (plainTextarea.value.length > 0) {
                    encryptBtn.disabled = false;
                } else {
                    encryptBtn.disabled = true;
                }
            } else {
                if (keyInputs[i].value.length > 0 && plainTextarea.value.length > 0) {
                    encryptBtn.disabled = false;
                } else {
                    encryptBtn.disabled = true;
                }
            }
        }
    };
    checkEncryptInput();
    // add event listeners to the inputs to re-validate the inputs when they change
    for (var i = 0; i < keyInputs.length; i++) {
        if (keyInputs[i].id != "no-key") {
            keyInputs[i].addEventListener("input", checkEncryptInput);
        }
    }
    plainTextarea.addEventListener("input", checkEncryptInput);
};

function clearTextarea() {
    document.getElementById("plainTextarea").value = "";
    document.getElementById("cipherTextarea").value = "";
    checkInput();
}

function encryptionData() {
    var selectedCipher = cipherSelect.value;
    var keyInputs = selectedCipherKeyInputFields();
    var plainTextValue = document.getElementById("plainTextarea").value;
    var inputForEncryption = {
        method: "encrypt",
        text: plainTextValue,
        keys: {}
    };
    if (keyInputs[0].id === "null") {
        inputForEncryption.keys[selectedCipher.toLowerCase()] = keyInputs[0].id;
    } else if (keyInputs.length === 1) {
        inputForEncryption.keys[selectedCipher.toLowerCase()] = keyInputs[0].value;
    } else {
        var keyValues = {};
        for (var i = 0; i < keyInputs.length; i++) {
            var input = keyInputs[i];
            keyValues[input.id] = input.value;
        }
        inputForEncryption.keys[selectedCipher.toLowerCase()] = keyValues;
    }
    console.log(inputForEncryption);
    return inputForEncryption;
}

function decryptionData() {
    //
}

// send the input to the views.py using fetch API
async function encryption() {
    const data = encryptionData();
    const response = await fetch(window.location.href, {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify(data)
    });
    const result = await response.text();
    document.getElementById("cipherTextarea").value = result;
}

document.getElementById("encryptBtn").addEventListener("click", encryption);
document.getElementById("clearBtn").addEventListener("click", clearTextarea);
document.getElementById("decryptBtn").addEventListener("click", encryptionData);


updateCiphers();
updateOperationDescription();
updateCipherDescription();
updateCipherKey();

checkInput();