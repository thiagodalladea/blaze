import { Link } from 'react-router-dom';
import styles from './FirstSection.module.css';
import cash_balance from '../../assets/cash_balance.png';

export function FirstSection(){
    return (
        <div className={ styles.firstSection }>
            <div className={ styles.txtimgContainer }>
                <div className={ styles.txtContainer }>
                    <h1>O <span className={ styles.differentColor }>Blaze Assistant</span> ajuda a <span className={ styles.differentColor }>alavancar</span> sua banca com mais <span className={ styles.differentColor }>eficiência</span>!</h1><br></br>
                    <p>Estatísticas e alarmes ao vivo dos jogos <span className={ styles.differentColor }>Crash</span> e <span className={ styles.differentColor }>Double</span> da Blaze.com <br></br>
                        Jogue de forma mais segura e assertiva! O assistente conta com um dashboard interativo de fácil usabilidade.
                    </p>
                </div>

                <div className={ styles.imgContainer }>
                    <img src={ cash_balance } alt='Money balance'/>
                </div>
            </div>
            <Link to='/dashboard' className={ styles.registerButton }> <button>Cadastrar-se</button> </Link>
        </div>
    )
}