/******************************************************************************************
// Implementation of the Template Design Pattern
/******************************************************************************************/

class Bio{
  constructor(bio, major, responsibilities, tests){
    this.bio = bio;
    this.major = major;
    this.responsibilities = responsibilities;
    this.tests = tests;
  }

  printFacts(bio, major, responsibilities, commits, issues, tests){
    document.getElementById("p1").innerHTML = "bio: " + bio;
    document.getElementById("p2").innerHTML = "major: " + major;
    document.getElementById("p3").innerHTML = "responsibilities: " + responsibilities;
    document.getElementById("p4").innerHTML = "commits: " + commits;
    document.getElementById("p5").innerHTML = "issues: " + issues;
    document.getElementById("p6").innerHTML = "unit tests: " + tests;
  }

  printBio(commits, issues){
    console.log("method not implemented")
  }
}


class ArjunBio extends Bio{

  constructor(bio, major, responsibilities, tests){
    super(bio, major, responsibilities, tests)
  }

  printBio(commits, issues){
    super.printFacts(this.bio, this.major, this.responsibilities, commits, issues, this.tests);
    document.getElementById("one").style.opacity = 1;
    document.getElementById("arjun").style.color = "rgb(76, 175, 80)";
    document.getElementById("two").style.opacity = 0.5;
    document.getElementById("blake").style.color = "black";
    document.getElementById("three").style.opacity = 0.5;
    document.getElementById("rabia").style.color = "black";
    document.getElementById("four").style.opacity = 0.5;
    document.getElementById("wenran").style.color = "black";
    document.getElementById("five").style.opacity = 0.5;
    document.getElementById("yinghong").style.color = "black";
  }
}

class BlakeBio extends Bio{

  constructor(bio, major, responsibilities, tests){
    super(bio, major, responsibilities, tests)
  }

  printBio(commits, issues){
    super.printFacts(this.bio, this.major, this.responsibilities, commits, issues, this.tests);
    document.getElementById("one").style.opacity = 0.5;
    document.getElementById("arjun").style.color = "black";
    document.getElementById("two").style.opacity = 1;
    document.getElementById("blake").style.color = "rgb(76, 175, 80)";
    document.getElementById("three").style.opacity = 0.5;
    document.getElementById("rabia").style.color = "black";
    document.getElementById("four").style.opacity = 0.5;
    document.getElementById("wenran").style.color = "black";
    document.getElementById("five").style.opacity = 0.5;
    document.getElementById("yinghong").style.color = "black";
  }
}


class RabiaBio extends Bio{

  constructor(bio, major, responsibilities, tests){
    super(bio, major, responsibilities, tests)
  }

  printBio(commits, issues){
    super.printFacts(this.bio, this.major, this.responsibilities, commits, issues, this.tests);
    document.getElementById("one").style.opacity = 0.5;
    document.getElementById("arjun").style.color = "black";
    document.getElementById("two").style.opacity = 0.5;
    document.getElementById("blake").style.color = "black";
    document.getElementById("three").style.opacity = 1;
    document.getElementById("rabia").style.color = "rgb(76, 175, 80)";
    document.getElementById("four").style.opacity = 0.5;
    document.getElementById("wenran").style.color = "black";
    document.getElementById("five").style.opacity = 0.5;
    document.getElementById("yinghong").style.color = "black";
  }
}

class WenranBio extends Bio{

  constructor(bio, major, responsibilities, tests){
    super(bio, major, responsibilities, tests)
  }

  printBio(commits, issues){
    super.printFacts(this.bio, this.major, this.responsibilities, commits, issues, this.tests);
    document.getElementById("one").style.opacity = 0.5;
    document.getElementById("arjun").style.color = "black";
    document.getElementById("two").style.opacity = 0.5;
    document.getElementById("blake").style.color = "black";
    document.getElementById("three").style.opacity = 0.5;
    document.getElementById("rabia").style.color = "black";
    document.getElementById("four").style.opacity = 1;
    document.getElementById("wenran").style.color = "rgb(76, 175, 80)";
    document.getElementById("five").style.opacity = 0.5;
    document.getElementById("yinghong").style.color = "black";
  }
}

class YinghongBio extends Bio{

  constructor(bio, major, responsibilities, tests){
    super(bio, major, responsibilities, tests)
  }

  printBio(commits, issues){
    super.printFacts(this.bio, this.major, this.responsibilities, commits, issues, this.tests);
    document.getElementById("one").style.opacity = 0.5;
    document.getElementById("arjun").style.color = "black";
    document.getElementById("two").style.opacity = 0.5;
    document.getElementById("blake").style.color = "black";
    document.getElementById("three").style.opacity = 0.5;
    document.getElementById("rabia").style.color = "black";
    document.getElementById("four").style.opacity = 0.5;
    document.getElementById("wenran").style.color = "black";
    document.getElementById("five").style.opacity = 1;
    document.getElementById("yinghong").style.color = "rgb(76, 175, 80)";
  }
}


/**********************************************************************************************
/*used the Class Extract refactoring method
/*********************************************************************************************/ 
class Developer{
      constructor(bio){
        this.bio = bio;
        this.commits = 0;
        this.issues = 0;
      }

      getCommit(){
            return this.commits;
      }

      getIssue(){
            return this.issues;
      }

      printBio(){
        this.bio.printBio(this.commits, this.issues);
      }
}


/**********************************************************************************************
/*Use of MVC Design Pattern
/*The Developer is our Model
/*about.html is our View
/*Control is our Controller
/*Used Method Extract on this function
/*********************************************************************************************/
class Controller{
  constructor(){
    this.Arjun = new Developer(new ArjunBio("I am Arjun Singh", "ECE", "engagement metric, rating page, unit tests, Reddit data scraping", "4"));
    this.Blake = new Developer(new BlakeBio("I am an Electrical Engineering major at the University of Texas", "ECE", "MySQL database, data scraping (games), games page, GCP", "6"));
    this.Rabia = new Developer(new RabiaBio("When I am not coding, I like going hiking", "ECE", "user stories, data scraping (games), games page", "0"));
    this.Wenran = new Developer(new WenranBio("I am a good dog walker", "ECE", "about page, consoles page, compare page, unit tests, data scraping (consoles)", "6"));
    this.Yinghong = new Developer(new YinghongBio("I am Yinghong Liu", "ME", "home page, 15 static pages", "0"));
    console.log("objects made");
  }

  highlightArjun(){
    this.Arjun.printBio();
  }

  highlightBlake(){
    this.Blake.printBio();
  }

  highlightRabia(){
    this.Rabia.printBio();
  }

  highlightWenran(){
    this.Wenran.printBio();
  }

  highlightYinghong(){
    this.Yinghong.printBio();
  }

  getTotalIssues(){
    return this.Arjun.getIssue() + this.Rabia.getIssue() + this.Blake.getIssue() + this.Yinghong.getIssue() + this.Wenran.getIssue()
  }

  getTotalCommits(){
    return this.Arjun.getCommit() + this.Rabia.getCommit() + this.Blake.getCommit() + this.Yinghong.getCommit() + this.Wenran.getCommit();
  }

  apiRequest(){
    var api = "https://api.github.com/repos/ArjunSingh1/SoftwareLab/issues";
    console.log("starting api request");
    $.get(api, function (data) {
      $.each(data, function (idx, obj) {
        if(obj.user.login == "rabiakhan713"){
          this.Rabia.issues += 1;
        } else if(obj.user.login == "wenranlu"){
          this.Wenran.issues += 1;
        } else if(obj.user.login == "Bgardner4"){
          this.Blake.issues += 1;
        } else if(obj.user.login == "YinghongLIU"){
          this.Yinghong.issues += 1;
        } else if(obj.user.login == "ArjunSingh1"){
          this.Arjun.issues += 1;
        }
      });
      var total = this.getTotalIssues();
      $("#totalIssues").append(total);
      console.log("finished issues");
    });
    api = "https://api.github.com/repos/ArjunSingh1/SoftwareLab/contributors"
    console.log("starting commits");
    $.get(api, function (data) {
      $.each(data, function (idx, obj) {
        if(obj.login == "rabiakhan713"){
          this.Rabia.commits += obj.contributions;
        } else if(obj.login == "wenranlu"){
          this.Wenran.commits += obj.contributions;
        } else if(obj.login == "Bgardner4"){
          this.Blake.commits += obj.contributions;
        } else if(obj.login == "YinghongLIU"){
          this.Yinghong.commits += obj.contributions;
        } else if(obj.login == "ArjunSingh1"){
          this.Arjun.commits += obj.contributions;
        }
      });
      var totalC = this.getTotalCommits();
      $("#totalCommits").append(totalC);
      console.log("finished commits");
    });              
  }
}

