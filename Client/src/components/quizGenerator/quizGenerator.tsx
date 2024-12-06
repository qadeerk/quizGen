import clsx from "clsx"
import { useState } from "react";

export default function QuizGenerator(props: any) {
    const [ActiveTab, setActiveTab] = useState('data');

    const dataTabActive = clsx(ActiveTab === "data" ? 'hc-active' : "")
    const jobDescriptionTabActive = clsx(ActiveTab === "job" ? 'hc-active' : "")
    const cvTabActive = clsx(ActiveTab === "cv" ? 'hc-active' : "")

    async function generateQuiz() {
        const dataText = (document.querySelector("#tab-data .hc-textarea") as HTMLTextAreaElement).value;
        const jobText = (document.querySelector("#tab-job .hc-textarea") as HTMLTextAreaElement).value;
        const cvText = (document.querySelector("#tab-cv .hc-textarea") as HTMLTextAreaElement).value;

        console.log("Data Tab Text:", dataText);
        console.log("Job Description Tab Text:", jobText);
        console.log("CV Tab Text:", cvText);

        const myHeaders = new Headers();
        myHeaders.append("Content-Type", "application/json");

        const requestOptions: RequestInit = {
            method: "POST",
            headers: myHeaders,
            body: JSON.stringify({"context": dataText , "jobDescription": jobText, "cvData": cvText}),
            redirect: "follow"
        };

        await fetch("http://localhost:8000/generateQuiz", requestOptions)
        .then((response) => response.text())
        .then((resultText) => {
            const result = JSON.parse(resultText);
            console.log(result);
            props.setQuizId(result.quiz_id);
        })
        .catch((error) => console.error(error))

        // props.setQuizId("76190d4c-aadd-4607-b3fb-61575a34973f");

    }

    return (
        <div className="hc-container">
            <div id="title" className="hc-title">Generate Quiz</div>

            <div id="tabs" className="hc-tabs">
                <div className="hc-tabs-header">
                    <button className={"hc-tab " + dataTabActive} data-tab="data" onClick={() => setActiveTab("data")}>Data</button>
                    <button className={"hc-tab " + jobDescriptionTabActive} data-tab="job" onClick={() => setActiveTab("job")}>Job Description</button>
                    <button className={"hc-tab " + cvTabActive} data-tab="cv" onClick={() => setActiveTab("cv")}>CV</button>
                </div>

                <div id="tab-data" className={"hc-tab-content " + dataTabActive}>
                    <div className="hc-section-title">Create Your Data Quiz</div>
                    <textarea className="hc-textarea" placeholder="Enter your text here..."></textarea>
                </div>

                <div id="tab-job" className={"hc-tab-content " + jobDescriptionTabActive}>
                    <div className="hc-section-title">Create Your Job Quiz</div>
                    <textarea className="hc-textarea" placeholder="Enter your text here..."></textarea>
                </div>

                <div id="tab-cv" className={"hc-tab-content " + cvTabActive}>
                    <div className="hc-section-title">Create Your CV Quiz</div>
                    <textarea className="hc-textarea" placeholder="Enter your text here..."></textarea>
                </div>
            </div>

            <div className="hc-btn-row">
                <button id="generate-quiz-btn" className="hc-generate-btn" onClick={()=>generateQuiz()}>Generate Quiz</button>
            </div>
        </div>
    )
}