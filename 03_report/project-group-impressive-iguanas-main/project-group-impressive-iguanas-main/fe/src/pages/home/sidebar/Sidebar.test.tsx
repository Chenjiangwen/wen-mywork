import { render, screen, fireEvent, act ,waitFor } from '@testing-library/react';
import { BrowserRouter } from 'react-router-dom';
import Sidebar from './Sidebar';

test('renders user info and project list when user is logged in', async () => {
  const response = {
    email: 'yyan998@gmail.com',
    projects: [
      {
        id: 'Happy-20Project-87131847',
        name: 'Happy project',
        envs: ['dev', 'prod'],
      },
      {
        id: 'Sad-project-1246234',
        name: 'Sad project',
        envs: ['dev', 'test', 'prod'],
      },
    ],
  };
  render(
    <BrowserRouter>
      <Sidebar response={response} />
    </BrowserRouter>
  );
  await waitFor(async () => {
    expect(screen.getByText("yyan998")).toBeInTheDocument();
    expect(screen.getByText('Happy project')).toBeInTheDocument();
    expect(screen.getByText('Sad project')).toBeInTheDocument();
    await act(async () => {
      fireEvent.click(screen.getByText('Happy project'));
    });
    expect(screen.getByText('dev')).toBeInTheDocument();
    await act(async () => {
      fireEvent.click(screen.getByText('dev'));
    });
    expect(window.location.pathname).toBe('/Happy-20Project-87131847/dev');
  });
});
