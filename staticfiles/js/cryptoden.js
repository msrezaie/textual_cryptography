// The var cipherSelect selects the HTML element with the ID of cipher-select,
// which is used later in the code to access the selected cipher.
var cipherSelect = document.getElementById("cipher-select");

// The var cipherKeyMap is an object that maps a cipher name to the name of its corresponding HTML element ID.
// It is used to dynamically change the display of the cipher key input fields depending on the selected cipher.
var cipherKeyMap = {
    "Caesar": "key-caesar",
    "Atbash": "key-none",
    "Affine": "key-affine",
    "Vigenere": "key-vigenere",
    "Reverse": "key-none",
    // "Feistel": "key-none",
    "Polybius": "key-none",
    "Four Square": "key-foursquare",
    "XOR": "key-xor",
};

// The selectedCipherKeyInputFields function gets the selected cipher and retrieves the corresponding HTML element ID from the cipherKeyMap.
// It then selects the input fields of the corresponding cipher key div using the querySelectorAll method.
function selectedCipherKeyInputFields() {
    var selectedCipher = cipherSelect.value;
    var selectedCipherKeyDiv = cipherKeyMap[selectedCipher];
    var selectedCipherKeyinputId = document.getElementById(selectedCipherKeyDiv);
    var keyInputs = selectedCipherKeyinputId.querySelectorAll("input");
    return keyInputs;
}

// The updateCiphers function updates the cipher selection dropdown menu based on the selected operation.
// It first selects the HTML element with the ID of operation-select and retrieves the value of the selected operation.
// It then retrieves the corresponding ciphers from an object called ciphers. For each cipher, the function checks if it is in the cipherKeyMap object.
// If it is, it adds the cipher as an option to the cipher selection dropdown menu. Otherwise, it adds a disabled option.
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

// The updateOperationDescription function updates the description of the selected operation based on the value of the HTML element with the ID of operation-select.
// It retrieves the corresponding description from an object called operationDescs and sets the HTML of the operation-desc element to the description.
function updateOperationDescription() {
    var operationId = document.getElementById("operation-select").value;
    // 'operationDesc' is taken from index.html
    var operationDesc = document.getElementById("operation-desc");
    var desc = operationDescs[operationId];

    operationDesc.innerHTML = desc;
}

// The updateCipherDescription function updates the description of the selected cipher based on the value of the HTML element with the ID of cipher-select.
// It retrieves the corresponding description from an object called cipherDescs and sets the HTML of the cipher-desc element to the description.
function updateCipherDescription() {
    var cipherName = document.getElementById("cipher-select").value;
    var cipherDesc = document.getElementById("cipher-desc");

    var desc = cipherDescs[cipherName];
    
    cipherDesc.innerHTML = desc;
}

// The updateCipherKey function updates the display of the cipher key input fields based on the selected cipher.
// It uses the selectedCipherKeyInputFields function to retrieve the selected cipher key input fields and then sets the display style of the corresponding cipher key div to "block".
// It also sets the value of all key input fields to an empty string.
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

// The caesarValidateInput, xorValidateInput, and affineValidateInput functions perform input validation on the corresponding cipher key input fields.
function caesarValidateInput(input) {
    if (input.value > 25) {
        input.value = 25;
    }
    input.value = input.value.replace(/[^0-9]/g, '');
}

function xorValidateInput(input) {
    if (input.value > 127) {
        input.value = 127;
    } else if (input.value < 0) {
        input.value = 0;
    }
    input.value = input.value.replace(/[^0-9]/g, '');
}

function affineValidateInput(input) {
    //
}

// The checkInput function checks if the required input fields have been filled out in order to enable the encryption and decryption buttons.
// It retrieves the key input fields and text areas using their corresponding HTML element IDs and then sets the disabled attribute of the encryption and decryption buttons based on whether or not the input fields have been filled out.
function checkInput() {
    var keyInputs = selectedCipherKeyInputFields();  
    var plainTextarea = document.getElementById("plainTextarea");
    var cipherTextarea = document.getElementById("cipherTextarea");

    const encryptBtn = document.getElementById("encryptBtn");
    const decryptBtn = document.getElementById("decryptBtn");

    function checkEncryptInput() {
        var numInputsWithValue = 0;
        var hasNullInput = false;

        for (var i = 0; i < keyInputs.length; i++) {
            if (keyInputs[i].id === "null") {
                hasNullInput = true;
            } else if (keyInputs[i].value.length > 0) {
                numInputsWithValue++;
            }
        }
        if (numInputsWithValue === keyInputs.length && plainTextarea.value.length > 0) {
            encryptBtn.disabled = false;
        } else if (hasNullInput && plainTextarea.value.length > 0) {
            encryptBtn.disabled = false;
        } else {
            encryptBtn.disabled = true;
        }
    };

    function checkDecryptInput() {
        var numInputsWithValue = 0;
        var hasNullInput = false;

        for (var i = 0; i < keyInputs.length; i++) {
            if (keyInputs[i].id === "null") {
                hasNullInput = true;
            } else if (keyInputs[i].value.length > 0) {
                numInputsWithValue++;
            }
        }
        if (numInputsWithValue === keyInputs.length && cipherTextarea.value.length > 0) {
            decryptBtn.disabled = false;
        } else if (hasNullInput && cipherTextarea.value.length > 0) {
            decryptBtn.disabled = false;
        } else {
            decryptBtn.disabled = true;
        }
    };

    checkEncryptInput();
    checkDecryptInput();
    // add event listeners to the inputs to re-validate the inputs when they change
    for (var i = 0; i < keyInputs.length; i++) {
        if (keyInputs[i].id != "null") {
            keyInputs[i].addEventListener("input", checkDecryptInput);
            keyInputs[i].addEventListener("input", checkEncryptInput);
        }
    }
    plainTextarea.addEventListener("input", checkEncryptInput);
    cipherTextarea.addEventListener("input", checkDecryptInput);
};


// The clearTextarea function sets the value of both the plain text and cipher text areas to an empty string and then calls the checkInput function.
function clearTextarea() {
    document.getElementById("plainTextarea").value = "";
    document.getElementById("cipherTextarea").value = "";
    document.getElementById("encryptBtn").disabled = true;
    document.getElementById("decryptBtn").disabled = true;
}


// The encryptionData function retrieves the selected cipher, the input text, and the selected key input fields.
// It then creates an object that includes these values and a "method" key set to "encrypt".
function encryptionData() {
    var selectedCipher = cipherSelect.value;
    var keyInputs = selectedCipherKeyInputFields();
    var plainTextValue = document.getElementById("plainTextarea").value;
    var inputForEncryption = {
        method: "encrypt",
        text: plainTextValue,
        cipher: selectedCipher.toLowerCase(),
    };
    if (keyInputs[0].id === "null") {
        inputForEncryption.keys = keyInputs[0].id;
    } else if (keyInputs.length === 1) {
        inputForEncryption.keys = keyInputs[0].value;
    } else {
        var keyValues = {};
        for (var i = 0; i < keyInputs.length; i++) {
            var input = keyInputs[i];
            keyValues[input.id] = input.value;
        }
        inputForEncryption.keys = keyValues;
    }
    return inputForEncryption;
}

// The decryptionData function is similar to encryptionData function that retrieves the selected cipher, the input text,
// and the selected key input fields. Only difference is that the key to its created object is set to "decrypt".
function decryptionData() {
    var selectedCipher = cipherSelect.value;
    var keyInputs = selectedCipherKeyInputFields();
    var cipherTextValue = document.getElementById("cipherTextarea").value;
    var inputForDecryption = {
        method: "decrypt",
        text: cipherTextValue,
        cipher: selectedCipher.toLowerCase(),
    };
    if (keyInputs[0].id === "null") {
        inputForDecryption.keys = keyInputs[0].id;
    } else if (keyInputs.length === 1) {
        inputForDecryption.keys = keyInputs[0].value;
    } else {
        var keyValues = {};
        for (var i = 0; i < keyInputs.length; i++) {
            var input = keyInputs[i];
            keyValues[input.id] = input.value;
        }
        inputForDecryption.keys = keyValues;
    }
    return inputForDecryption;
}

// 'encryption()' sends data to the server-side views.py using the fetch API with a POST request.
// The request includes the data in JSON format as the request body. The response from the server is then received and converted to text.
// The resulting text is assigned to the value property of the element with ID "cipherTextarea". Finally, the checkInput() function is called.
async function encryption() {
    const data = encryptionData();
    const response = await fetch(window.location.href, {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify(data)
    });
    const result = await response.text();
    document.getElementById("cipherTextarea").value = result;
    checkInput();
}

// Similarly, 'decryption()' sends data to the server-side views.py using the fetch API with a POST request.
// The request includes the data in JSON format as the request body. The response from the server is then received and converted to text.
// The resulting text is assigned to the value property of the element with ID "plainTextarea". Finally, the checkInput() function is called.
async function decryption() {
    const data = decryptionData();
    const response = await fetch(window.location.href, {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify(data)
    });
    const result = await response.text();
    document.getElementById("plainTextarea").value = result;
    checkInput();
}

document.getElementById("encryptBtn").addEventListener("click", encryption);
document.getElementById("decryptBtn").addEventListener("click", decryption);
document.getElementById("clearBtn").addEventListener("click", clearTextarea);

// Calling necessary functions at the start of the application
updateCiphers();
updateOperationDescription();
updateCipherDescription();
updateCipherKey();

checkInput();