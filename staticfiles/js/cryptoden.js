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
    var ciphers = operations[operationId];

    cipherSelect.innerHTML = "";
    if (ciphers) {
        for (var i = 0; i < ciphers.length; i++) {
            cipherSelect.innerHTML += "<option value='" + ciphers[i] + "'>" + ciphers[i] + "</option>";
        }
    } else {
        cipherSelect.innerHTML = "<option value=''>Select Operation First</option>";
    }
}

function updateOperationDescription() {
    var operationId = document.getElementById("operation-select").value;
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
            if (keyInputs[i].id == "no-key") {
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
    var keyInputs = selectedCipherKeyInputFields();
    var plainTextValue = document.getElementById("plainTextarea").value;
    var inputForEncryption = {
        plainText: plainTextValue,
        keys: {},
    };
    for (var i = 0; i < keyInputs.length; i++) {
        var input = keyInputs[i];
        if (input.id == "no-key") {
            inputForEncryption.keys[input.id] = "None";
        } else {
            inputForEncryption.keys[input.id] = input.value;
        }
    }
}

// function encryption() {
//     let plainText = document.getElementById("plainTextarea").value;
//     let caesarKey = document.getElementById("caesar-key").value;

//     // send the input to the views.py using AJAX
//     const xhr = new XMLHttpRequest();
//     xhr.open("POST", window.location.href, true);
//     xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
//     xhr.onreadystatechange = function() {
//         if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
//         // get the response and display it in the cipherTextarea
//             document.getElementById("cipherTextarea").value = this.responseText;
//         }
//     };
//     xhr.send(`plainText=${plainText}&caesarKey=${caesarKey}`);
// }

document.getElementById("encryptBtn").addEventListener("click", encryptionData);
document.getElementById("clearBtn").addEventListener("click", clearTextarea);
document.getElementById("decryptBtn").addEventListener("click", updateCiphers);


updateCiphers();
updateOperationDescription();
updateCipherDescription();
updateCipherKey();

checkInput();