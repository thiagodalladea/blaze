import './global.css';
import { LoginHeader } from './components/WelcomePage/LoginHeader.js';
import { FirstSection } from './components/WelcomePage/FirstSection.js';

export function WelcomePage() {
  return (
    <>
      <LoginHeader />
      <FirstSection />
    </>
  );
}