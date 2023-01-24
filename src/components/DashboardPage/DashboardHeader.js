import { Link } from 'react-router-dom';
import styles from './DashboardHeader.module.css';
import logo from '../../assets/logo.svg'
import sidebar_icon from '../../assets/sidebar_icon.svg'
import profile_icon from '../../assets/profile_icon.svg'

export function DashboardHeader(){
    return (
        <div className={ styles.header }>
            <div className={ styles.sidebarIcon }>
                <img src={ sidebar_icon } alt='Sidebar icon'/>
            </div>

            <Link to='/dashboard' className={ styles.logo }>
                <img src={ logo } alt='Blaze Assistant logo'/>
            </Link>

            <Link to='/profile' className={ styles.profileIcon }>
                <img src={ profile_icon } alt='Blaze Assistant logo'/>
                <p>Acessar perfil</p>
            </Link>
        </div>
    )
}