const generateQuizRequestAll = async (formData: any) => {
  try {
    const response = await fetch("http://localhost:8000/generateQuiz/", {
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

const generateQuizRequestFromJobDescription = async (formData: any) => {
  try {
    const response = await fetch("http://localhost:8000/generateQuiz/jobdescription", {
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
    // alert("Failed to upload data.");
  }
};

const streamGenerateQuizRequestFromJobDescription = async (formData: any, setCurrentPhase: Function) => {
  const url = "http://localhost:8000/generateQuiz/jobdescription/v2"; // Update the URL

  try {
    // Make a POST fetch request to the server
    const response = await fetch(url, {
      method: "POST",
      body: formData
    });

    // Check if the response is OK
    if (!response.ok) {
      console.error("Failed to connect to the server:", response.statusText);
      return;
    }

    // Get the readable stream from the response
    const reader = response.body.getReader();
    const decoder = new TextDecoder("utf-8");
    let quizId = null;
    let buffer = ""; // Buffer to hold incomplete JSON chunks

    // Start reading the stream
    while (true) {
      const { value, done } = await reader.read();

      if (done) {
        console.log("Stream closed by the server.");
        break;
      }

      // Decode and process the streamed data
      buffer += decoder.decode(value, { stream: true }).trim();

      // Process the JSON data
      try {
        // Split the buffer by the closing brace of JSON objects
        const parts = buffer.split(/(?<=})/);

        for (let i = 0; i < parts.length - 1; i++) {
          const parsedChunk = JSON.parse(parts[i]);
          setCurrentPhase(parsedChunk.event);
          console.log("Event received:", parts[i]);

          // Handle specific events
          if (parsedChunk && parsedChunk.quiz_id) {
            quizId = parsedChunk.quiz_id;
          }
        }

        // Keep the last part in the buffer (it might be incomplete)
        buffer = parts[parts.length - 1];
      } catch (error) {
        console.log("Event received:", buffer);
        setCurrentPhase(buffer);
        console.error("Failed to parse chunk as JSON:", buffer, error);
      }
    }

    return { 'quizId': quizId };
  } catch (error) {
    console.error("Error while streaming events:", error);
  }
};

const generateQuizRequestFromContext = async (formData: any) => {
  try {
    const response = await fetch("http://localhost:8000/generateQuiz/", {
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

export { generateQuizRequestAll, generateQuizRequestFromJobDescription, generateQuizRequestFromContext, streamGenerateQuizRequestFromJobDescription };
