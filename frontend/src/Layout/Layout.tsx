import { Outlet } from 'react-router-dom';
import './Layout.css';

function Layout() {
    return(
        <main>
            <div className="content">
                <Outlet />
            </div>
        </main>
    )
}

export default Layout;
