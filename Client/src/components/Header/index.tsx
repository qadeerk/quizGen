import { useLocation, useNavigate } from 'react-router-dom';
import { useMemo } from 'react';

export default function AppHeader() {
    const location = useLocation();
    const navigate = useNavigate();
    const queryParams = useMemo(() => new URLSearchParams(location.search), [location.search]);

    const handleLogoClick = () => {
        navigate('/');
    };

    const handleGenerateQuizClick = () => {
        navigate('/generate');
    };

    const handleTestEditBtnClick = () => {
        navigate('/edit?quizId=530ba1eb-6968-4afc-b980-5da21c597c14');
    };
    const handleTestEvaluationBtnClick = () => {
        navigate('/evaluation?quizId=530ba1eb-6968-4afc-b980-5da21c597c14');
    };
    const handleTestReportBtnClick = () => {
        
        navigate('/report');
    };

    return <header className="hc-header">
        <div className="hc-header-logo" onClick={handleLogoClick} style={{ cursor: 'pointer' }}>Hire IQ</div>
        {queryParams.has('test') && (
            <>
            <button className="hc-theme-toggle" id="testButton" onClick={handleTestEditBtnClick}>test edit</button>
            <button className="hc-theme-toggle" id="testButton" onClick={handleTestEvaluationBtnClick}>test evaluation</button>
            <button className="hc-theme-toggle" id="testButton" onClick={handleTestReportBtnClick}>test Report</button>
            </>
        )}
        {location.pathname === '/' && (
            <button className="hc-theme-toggle" id="themeToggle" onClick={handleGenerateQuizClick}>Generate Quiz</button>
        )}
    </header>
}