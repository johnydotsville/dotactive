import ReactDOM from 'react-dom/client';

import { App } from '@components/App';

import { MyDatabase } from '@domain/database/MyDatabase';


async function prepare() {
  const database = MyDatabase.getInstance();
  await database.init();

  const root = ReactDOM.createRoot(document.getElementById('root'));
  root.render(
    <App database={database} />
  );
}

prepare();