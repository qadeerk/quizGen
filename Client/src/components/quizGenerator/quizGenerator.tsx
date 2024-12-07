import clsx from "clsx"
import { useEffect, useState } from "react";
import sendQuizRequest from "./utils";

export default function QuizGenerator(props: any) {
    const [ActiveTab, setActiveTab] = useState('data');
    const [jobDescription, setJobDescription] = useState("test");

    const dataTabActive = clsx(ActiveTab === "data" ? 'hc-active' : "")
    const jobDescriptionTabActive = clsx(ActiveTab === "job" ? 'hc-active' : "")
    const cvTabActive = clsx(ActiveTab === "cv" ? 'hc-active' : "")

    useEffect(() => {
        console.log("Fetching job description");
        fetch("http://localhost:5173/public/jobdescription.txt")
            .then((response) => {
                if (!response.ok) {
                    throw new Error("Failed to fetch the text file");
                }
                return response.text();
            })
            .then((data) => {
                console.log(data);
                setJobDescription(data)
            })
    }
    , [])

    async function generateQuiz() {
        const formData = new FormData();
        formData.append("context", (document.querySelector("#tab-data .hc-textarea") as HTMLTextAreaElement).value);
        formData.append("jobDescription",(document.querySelector("#tab-job .hc-textarea") as HTMLTextAreaElement).value);

        const fileInput = document.querySelector("#pdf_doc") as HTMLInputElement;

        
        if (fileInput?.files && fileInput.files[0]) {
            formData.append("file", fileInput.files[0]);
        }

        const response = await sendQuizRequest(formData);

        console.log(response);
        debugger;
        props.setQuizId(response.quizId);
        props.setMatchingAttributes(response.matchingAtrubuted);
        props.setuniqueAttributes(response.nonMatchingAtrubuted);
        // props.setQuizId("530ba1eb-6968-4afc-b980-5da21c597c14");

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
                    <textarea className="hc-textarea" placeholder="Enter your text here..." value={jobDescription} onChange={(t) => setJobDescription(t.target.value)}></textarea>
                </div>

                <div id="tab-cv" className={"hc-tab-content " + cvTabActive}>
                    <div className="hc-section-title">Create Your CV Quiz</div>
                    {/* <textarea className="hc-textarea" placeholder="Enter your text here..."></textarea> */}
                    <input type="file" name="pdf_doc" id="pdf_doc" accept=".pdf" className=" drop-shadow-md bg-white/10 font-semibold leading-6 text-gray-900 border border-blue-300 py-2 px-4 rounded-2xl block w-full text-sm text-slate-500
                                                        file:mr-4 file:py-2 file:px-4
                                                        file:rounded-full file:border-0
                                                        file:text-sm file:font-semibold
                                                        file:bg-blue-50 file:text-blue-400
                                                        hover:file:bg-blue-100"></input>
                </div>
            </div>

            <div className="hc-btn-row">
                <button id="generate-quiz-btn" className="hc-generate-btn" onClick={() => generateQuiz()}>Generate Quiz</button>
            </div>
        </div>
    )
}