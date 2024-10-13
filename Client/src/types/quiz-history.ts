export type QuizHistory = {
    id: number,
    name: string,
    questions: {
        question: string,
        answer: string,
    }[]
}[]