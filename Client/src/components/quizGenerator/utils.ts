const sendQuizRequest = async (formData: any) => {
    try {

      // const requestOptions = {
      //   method: "POST",
      //   body: formData,
      //   redirect: "follow"
      // };
      
      // fetch("http://localhost:8000/generateQuiz/v2", requestOptions: any)
      //   .then((response) => response.text())
      //   .then((result) => console.log(result))
      //   .catch((error) => console.error(error));

        const response = await fetch("http://localhost:8000/generateQuiz/v2", {
          method: "POST",
          body: formData,
          redirect: "follow"
        });
    
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
    
        const data = await response.json();
        console.log("Success:", data);
        return data;

      } catch (error) {
        console.error("Error:", error);
        alert("Failed to upload data.");
      }
};

export default sendQuizRequest;
