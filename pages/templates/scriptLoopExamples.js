<script>
    var nameArray = [
        "Jimmy",
        "Sonny",
        "Sammy",
        "Henry",
        "Hank",
        "Susan",
        "Sebby",
        "Alyssa",
        "Pepper",
        "Ken",
        "Steve",
        "Kandi",
        "Wes"
        ];
      var numberStudents = nameArray.length;
      var interval;

      for(n = 0; n < numberStudents; n++){
            var divName = "floatName" + n;
            console.log(divName);
            var names = nameArray[n];
            var divTag = document.createElement('div');
            divTag.id = divName;
            divTag.innerHTML = names;
            divTag.style.position = "absolute";
            divTag.style.top = 50 + n*20 + "px";
            divTag.style.left  = "50px";
            divTag.className = "randomFloat";
            document.body.appendChild(divTag);

                      };
              var loopAllowed = false;
              $( "#go" ).click(function() {
                loopAllowed = true;
                var max = 12;
                var loop = function(){
                  for(i = 0; i < (numberStudents + 1); i++){
                    var divName = "floatName" + i;
                    console.log(divName);
                    $( "#" + divName ).animate({
                        left: Math.random()*500 + "px",
                        top: Math.random()*500 + "px"
                    }, 500, i == max - 1 && loopAllowed ? loop : undefined);
                  }
                 };
                 loop();
                });

              $( "#stop" ).click(function() {
                    loopAllowed = false;
              });

        </script>


 
// Now Django it 
//Build Inheriting Templates

{% block body %}

    <div class="container">
        <div class="row">
            <div class="twelve columns">
                <h1>Choose the block</h1>
            </div>
        </div>
        <!-- SNIP ... -->
    </div>

{% endblock %}

{% block extra_js %}
    <script>
        var nameArray = [
            "Jimmy",
            "Sonny",
            "Sammy",
            "Henry",
            "Hank",
            "Susan",
            "Sebby",
            "Alyssa",
            "Pepper",
            "Ken",
            "Steve",
            "Kandi",
            "Wes"
        ];
        var numberStudents = nameArray.length;
        var interval;
        // SNIP ..
    </script>
{% endblock extra_js %}



var a3 = [
    {{ times.facility }}
    {{ times.address }}
    {{ times.city }}
    {{ times.state }}
    {{ times.zipcode }}
];

var a3List = a3.length;
var interval;

            

