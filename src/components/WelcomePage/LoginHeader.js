import { Link } from 'react-router-dom';
import styles from './LoginHeader.module.css';
import logo from '../../assets/logo.svg';
import sidebar_icon from '../../assets/sidebar_icon.svg';

export function LoginHeader(){
    return (
        <div className={ styles.header }>
            <div className={ styles.sidebarIcon }>
                <img src={ sidebar_icon } alt='Sidebar icon'/>
            </div>

            <Link to='/' className={ styles.logo }>
                <img src={ logo } alt='Blaze Assistant logo'/>
            </Link>

            <Link to='/dashboard' className={ styles.loginInfo }>
                <p>Entrar</p>
                <button>Cadastrar-se</button>
            </Link>
        </div>
    )
}