TL_ENABLED_TEXT = "<a href='javascript:;' onclick='tlinject_revert()'>禁用翻译</a> " +
                  "(<a href='javascript:;' onclick='tlinject_about()'>啥玩意？</a>)"
TL_DISABLED_TEXT = "<a href='javascript:;' onclick='tlinject_activate()'>启用翻译</a> " +
                   "(<a href='javascript:;' onclick='tlinject_about()'>啥东西？</a>)"

function load_translations(trans, cb) {
    var xhr = new XMLHttpRequest()
    xhr.open("POST", "/api/v1/read_tl", true)
    xhr.setRequestHeader("Content-Type", "application/json; charset=utf-8")
    xhr.setRequestHeader("X-Blessing",
        "This request bears the blessing of an Ascended Constituent of the Summer Triangle, granting it the entitlement of safe passage.")
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            returned_list = JSON.parse(xhr.responseText)
            cb(returned_list)
        }
    }
    xhr.send(JSON.stringify(trans))
}

function submit_tl_string(node, text) {
    var sub = prompt("'" + text + "' 的翻译是啥？？？\n\n" +
        "* 这些你提交的字串可能会被作为公共数据导出的一部分而被公开。这些数据导出【并不会】包含任何能够识别你的信息，如果你是手滑或者不同意，点取消。");

    if (sub === null) return

    var xhr = new XMLHttpRequest()
    xhr.open("POST", "/api/v1/send_tl", true)
    xhr.setRequestHeader("Content-Type", "application/json; charset=utf-8")
    xhr.setRequestHeader("X-Blessing",
        "This request bears the blessing of an Ascended Constituent of the Summer Triangle, granting it the entitlement of safe passage.")
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            var table = {}
            table[text] = sub;
            set_strings_by_table(table)
        }
    }
    xhr.send(JSON.stringify({key: text, tled: sub, security: node.getAttribute("data-summertriangle-assr")}))
}

function set_strings_by_table(table) {
    var strings = document.getElementsByClassName("tlable")
    for (var i = 0; i < strings.length; i++) {
        strings[i].textContent = table[strings[i].getAttribute("data-original-string")] || strings[i].textContent;
    }
}

function tlinject_activate() {
    var tls = []
    var strings = document.getElementsByClassName("tlable")
    if (strings.length == 0) return;

    for (var i = 0; i < strings.length; i++) {
        if (tls.indexOf(strings[i].textContent) == -1)
            tls.push(strings[i].textContent);
        strings[i].setAttribute("data-original-string", strings[i].textContent);
        if (strings[i].hasAttribute("data-summertriangle-assr"))
            strings[i].setAttribute("onclick", "event.preventDefault(); submit_tl_string(this, this.getAttribute('data-original-string'))")
    }

    load_translations(tls, function(tls2) {
        for (var i = 0; i < strings.length; i++) {
            strings[i].textContent = tls2[strings[i].textContent] || strings[i].textContent;
        }
        var insert = 0;
        var node = document.body.querySelector(".crowd_tl_notice");
        if (!node) {
            node = document.createElement("div");
            node.className = "crowd_tl_notice";
            insert = 1;
        }
        node.innerHTML = TL_ENABLED_TEXT;
        if (insert) document.body.insertBefore(node, document.body.childNodes[0]);
    })
}

function tlinject_revert() {
    var strings = document.getElementsByClassName("tlable")
    for (var i = 0; i < strings.length; i++) {
        strings[i].textContent = strings[i].getAttribute("data-original-string");
    }
    document.body.querySelector(".crowd_tl_notice").innerHTML = TL_DISABLED_TEXT;
}

function tlinject_about() {
    var banner = "此站包含众包翻译。如果有句子在你悬停在上面时高亮显示，你可以点击并提交翻译。";
    alert(banner);
}
