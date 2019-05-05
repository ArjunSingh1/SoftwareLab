class Developer{
      constructor(id, bio, major, responsibilities, tests){
            this.id = id;
            this.bio = bio;
            this.major = major;
            this.responsibilities = responsibilities;
            this.commits = 0;
            this.issues = 0;
            this.tests = tests;
      }

      getCommit(){
            return this.commits;
      }

      getIssue(){
            return this.issues;
      }

      printBio(){
            document.getElementById("p1").innerHTML = "bio: " + this.bio;
            document.getElementById("p2").innerHTML = "major: " + this.major;
            document.getElementById("p3").innerHTML = "responsibilities: " + this.responsibilities;
            document.getElementById("p4").innerHTML = "commits: " + this.commits;
            document.getElementById("p5").innerHTML = "issues: " + this.issues;
            document.getElementById("p6").innerHTML = "unit tests: " + this.tests;

            if(this.id == 1) {
                  document.getElementById("one").style.opacity = 1;
                  document.getElementById("arjun").style.color = "rgb(76, 175, 80)";
            } else{
                  document.getElementById("one").style.opacity = 0.5;
                  document.getElementById("arjun").style.color = "black";
            }

            if(this.id == 2) {
                  document.getElementById("two").style.opacity = 1;
                  document.getElementById("blake").style.color = "rgb(76, 175, 80)";
            } else {
                  document.getElementById("two").style.opacity = 0.5;
                  document.getElementById("blake").style.color = "black";
            }

            if(this.id == 3) {
                  document.getElementById("three").style.opacity = 1;
                  document.getElementById("rabia").style.color = "rgb(76, 175, 80)";
            } else {
                  document.getElementById("three").style.opacity = 0.5;
                  document.getElementById("rabia").style.color = "black";
            }
            
            if(this.id == 4) {
                  document.getElementById("four").style.opacity = 1;
                  document.getElementById("wenran").style.color = "rgb(76, 175, 80)";
            } else {
                  document.getElementById("four").style.opacity = 0.5;
                  document.getElementById("wenran").style.color = "black";
            }

            if(this.id == 5) {
                  document.getElementById("five").style.opacity = 1;
                  document.getElementById("yinghong").style.color = "rgb(76, 175, 80)";
            } else {
                  document.getElementById("five").style.opacity = 0.5;
                  document.getElementById("yinghong").style.color = "black";
            }
      }
}

function apiRequest(Arjun, Blake, Rabia, Wenran, Yinghong){
                var api = "https://api.github.com/repos/ArjunSingh1/SoftwareLab/issues";
                $.get(api, function (data) {
                    $.each(data, function (idx, obj) {
                        if(obj.user.login == "rabiakhan713"){
                            Rabia.issues += 1;
                        } else if(obj.user.login == "wenranlu"){
                            Wenran.issues += 1;
                        } else if(obj.user.login == "Bgardner4"){
                            Blake.issues += 1;
                        } else if(obj.user.login == "YinghongLIU"){
                            Yinghong.issues += 1;
                        } else if(obj.user.login == "ArjunSingh1"){
                            Arjun.issues += 1;
                        }
                    });
                    var total = Arjun.getIssue() + Rabia.getIssue() + Blake.getIssue() + Yinghong.getIssue() + Wenran.getIssue();
                    $("#totalIssues").append(total);
                });
                api = "https://api.github.com/repos/ArjunSingh1/SoftwareLab/contributors"
                $.get(api, function (data) {
                    $.each(data, function (idx, obj) {
                        if(obj.login == "rabiakhan713"){
                            Rabia.commits += obj.contributions;
                        } else if(obj.login == "wenranlu"){
                            Wenran.commits += obj.contributions;
                        } else if(obj.login == "Bgardner4"){
                            Blake.commits += obj.contributions;
                        } else if(obj.login == "YinghongLIU"){
                            Yinghong.commits += obj.contributions;
                        } else if(obj.login == "ArjunSingh1"){
                            Arjun.commits += obj.contributions;
                        }
                    });
                    var totalC = Arjun.getCommit() + Rabia.getCommit() + Blake.getCommit() + Yinghong.getCommit() + Wenran.getCommit();
                    $("#totalCommits").append(totalC);
                });
}