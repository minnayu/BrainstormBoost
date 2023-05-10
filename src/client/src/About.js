import React from "react";

function About() {
    return (
        <div>
            <h1 class="display-4 text-center">Meet the Team</h1>
            <div class="d-flex p-2 justify-content-evenly">
                <div class="card" style={{width: "18rem "}}>
                    <img src="https://media.licdn.com/dms/image/C4E03AQG3pw5TF6KKiA/profile-displayphoto-shrink_400_400/0/1516783050633?e=1688601600&v=beta&t=aDNXg3Qls1yNUIL6_8O9O0HVxqnh5Uwc8qOHXmbwz9c" class="card-img-top" alt="Gilberto Arellano smiling and wearing a bow tie"/>
                    <div class="card-body">
                        <h5 class="mb-2 lead"><strong>Gilberto Arellano</strong></h5>
                        <p class="text-muted lead">Gilberto description</p>
                    </div>
                    <div class="card-body d-flex justify-content-evenly">
                        <a href="https://www.linkedin.com/in/gilbertoarellano/" target="_blank" class="fa fa-linkedin"></a>
                        <a href="https://github.com/gilarellano" target="_blank" class="fa fa-github"></a>
                    </div>
                </div>

                <div class="card" style={{width: "18rem "}}>
                    <img src="https://media.licdn.com/dms/image/C4E03AQEFuTcAteqxMw/profile-displayphoto-shrink_400_400/0/1634858398048?e=1688601600&v=beta&t=yJhc2POOBoA9r-eJibUaTfMdrMPLCcxbgxhvU3H4GcI" class="card-img-top" alt="Luis Rivas smiling in a white button up with pineapples"/>
                    <div class="card-body">
                        <h5 class="mb-2 lead"><strong>Luis Rivas</strong></h5>
                        <p class="text-muted lead">Luis studies Software Engineering and Analytics at Chapman University. In his free time he enjoys gaming and investing.</p>
                    </div>
                    <div class="card-body d-flex justify-content-evenly">
                        <a href="https://www.linkedin.com/in/luisnicolasrivas/" target="_blank" class="fa fa-linkedin"></a>
                        <a href="https://github.com/Lnrivas" target="_blank" class="fa fa-github"></a>
                    </div>
                </div>

                <div class="card" style={{width: "18rem "}}>
                    <img src="https://media.licdn.com/dms/image/C4D03AQFtnaGAasyykA/profile-displayphoto-shrink_400_400/0/1639712520327?e=1688601600&v=beta&t=WcD8JZfh2Q6pEE9fR934TdR_8rFnQ_XyAjhXKama3Z0" class="card-img-top" alt="Minna Yu smiling in front of LACMA 'Urban Light'"/>
                    <div class="card-body">
                        <h5 class="mb-2 lead"><strong>Minna Yu</strong></h5>
                        <p class="text-muted lead">Minna is a Software Engineering major at Chapman University. She is particularly interested in web design and drinking honey lavender lattes.</p>
                    </div>
                    <div class="card-body d-flex justify-content-evenly">
                        <a href="https://www.linkedin.com/in/minna-yu-54ab531bb/" target="_blank" class="fa fa-linkedin"></a>
                        <a href="https://github.com/minnayu" target="_blank" class="fa fa-github"></a>
                    </div>
                </div>

            </div>
        </div>

    );
}
export default About;
