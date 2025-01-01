import { Button } from '../button/button';
import styles from './evaluate.module.css';

type EvaluationPanelProps = {
  type: 'main' | 'secondary' | 'tertiary';
  title: string;
  description: string;
  instructions?: string;
  buttonText?: string;
  buttonAction?: () => void;
};

export default function EvaluationPanel({ 
  type, 
  title, 
  description, 
  instructions, 
  buttonText, 
  buttonAction 
}: EvaluationPanelProps) {
  return (
    <div className={type === 'main' ? styles.quizStart : type === 'secondary' ? styles.sectionStart : styles.thankYouScreen}>
      <h1>{title}</h1>
      <p>{description}</p>
      {instructions && <p>{instructions}</p>}
      {buttonText && buttonAction && <Button variant="primary" size="medium" onClick={buttonAction}>{buttonText}</Button>}
    </div>
  );
}
