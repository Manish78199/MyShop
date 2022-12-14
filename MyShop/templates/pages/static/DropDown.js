
        var toggle = document.querySelectorAll(".toggle_btn");

        toggle.forEach((tog) => {
            tog.onclick = function () {

                var own = this;
                own.classList.add("Active_toggle")
                document.querySelector(this.dataset.toggle).classList.add("show_drop");
                var what = this.dataset.toggle;
                document.onmouseup = function (e) {
                   
                    e.preventDefault();

                    /*var ha = true;
                    for (let i of e.path) {
                        if (i == document.querySelector(what)) {
                            ha = false;
                            break;

                        }

                    }
                    if (ha) */{

                        document.querySelector(what).classList.remove("show_drop");
                        own.classList.remove("Active_toggle")
                    }


                }
                var allvalues=document.querySelectorAll(".DropDown_values");
                allvalues.forEach((val)=>{
                    val.onclick=function(){
                         document.querySelector(what).classList.remove("show_drop");
                         own.classList.remove("Active_toggle")
                        document.querySelector("#drop_text").innerHTML=String(this.innerHTML).length >11?String(this.innerHTML).slice(0,9)+"...":this.innerHTML;
                    }
                });
            }
        });
