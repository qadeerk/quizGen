import { useSearchParams } from "react-router-dom";
import styles from "./publish.module.scss";
import { Button } from '../button/button';

export default function Publish() {
    const [searchParams] = useSearchParams();
    const quizId = searchParams.get('quizId');

    if (!quizId) {
        return <div>quizId not found</div>;
    }

    const currentUrl = window.location.href;
    const newUrl = currentUrl.replace("/publish", "/evaluation");

    const handleCopyUrl = () => {
        navigator.clipboard.writeText(newUrl).catch(err => console.error(err));
    };

    return (
        <div className={styles.publishContainer}>
            <div className={styles.publishBox}>
                <div
                    className={styles.publishLink}
                    onClick={() => window.open(newUrl, "_self")}
                    title={newUrl}
                >
                    {newUrl}
                </div>
                <Button onClick={handleCopyUrl}>Copy URL</Button>
            </div>
        </div>
    );
}
