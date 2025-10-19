import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import { jest } from '@jest/globals';
import Card from './Card';

describe('Card', () => {
  test('renders basic card', () => {
    render(
      <Card>
        <div>Card content</div>
      </Card>
    );
    
    const card = screen.getByText('Card content').closest('.ds-card');
    expect(card).toBeInTheDocument();
    expect(card).toHaveClass('ds-card', 'ds-card--default', 'ds-card--padding-medium', 'ds-card--shadow-base');
  });

  test('renders different variants', () => {
    const { rerender } = render(<Card variant="primary">Content</Card>);
    expect(screen.getByText('Content').closest('.ds-card')).toHaveClass('ds-card--primary');
    
    rerender(<Card variant="success">Content</Card>);
    expect(screen.getByText('Content').closest('.ds-card')).toHaveClass('ds-card--success');
  });

  test('renders different padding sizes', () => {
    const { rerender } = render(<Card padding="small">Content</Card>);
    expect(screen.getByText('Content').closest('.ds-card')).toHaveClass('ds-card--padding-small');
    
    rerender(<Card padding="large">Content</Card>);
    expect(screen.getByText('Content').closest('.ds-card')).toHaveClass('ds-card--padding-large');
  });

  test('renders different shadow levels', () => {
    const { rerender } = render(<Card shadow="sm">Content</Card>);
    expect(screen.getByText('Content').closest('.ds-card')).toHaveClass('ds-card--shadow-sm');
    
    rerender(<Card shadow="lg">Content</Card>);
    expect(screen.getByText('Content').closest('.ds-card')).toHaveClass('ds-card--shadow-lg');
  });

  test('handles interactive state', () => {
    const handleClick = jest.fn();
    render(
      <Card interactive onClick={handleClick}>
        Interactive card
      </Card>
    );
    
    const card = screen.getByText('Interactive card').closest('.ds-card');
    expect(card).toHaveClass('ds-card--interactive');
    expect(card).toHaveAttribute('role', 'button');
    expect(card).toHaveAttribute('tabIndex', '0');
    
    fireEvent.click(card);
    expect(handleClick).toHaveBeenCalledTimes(1);
  });

  test('supports custom className', () => {
    render(<Card className="custom-card">Content</Card>);
    
    expect(screen.getByText('Content').closest('.ds-card')).toHaveClass('custom-card');
  });

  test('supports ARIA attributes', () => {
    render(
      <Card 
        aria-label="Custom card"
        aria-labelledby="card-title"
        aria-describedby="card-description"
      >
        Content
      </Card>
    );
    
    const card = screen.getByText('Content').closest('.ds-card');
    expect(card).toHaveAttribute('aria-label', 'Custom card');
    expect(card).toHaveAttribute('aria-labelledby', 'card-title');
    expect(card).toHaveAttribute('aria-describedby', 'card-description');
  });

  test('supports custom role', () => {
    render(<Card role="article">Content</Card>);
    
    expect(screen.getByText('Content').closest('.ds-card')).toHaveAttribute('role', 'article');
  });

  test('supports custom tabIndex', () => {
    render(<Card interactive tabIndex={-1}>Content</Card>);
    
    expect(screen.getByText('Content').closest('.ds-card')).toHaveAttribute('tabIndex', '-1');
  });

  test('forwards ref correctly', () => {
    const ref = React.createRef();
    render(<Card ref={ref}>Content</Card>);
    
    expect(ref.current).toBeInstanceOf(HTMLDivElement);
  });

  test('passes through additional props', () => {
    render(<Card data-testid="custom-card" title="Card title">Content</Card>);
    
    const card = screen.getByTestId('custom-card');
    expect(card).toHaveAttribute('title', 'Card title');
  });
});

describe('Card.Header', () => {
  test('renders card header', () => {
    render(
      <Card>
        <Card.Header>Header content</Card.Header>
      </Card>
    );
    
    const header = screen.getByText('Header content');
    expect(header.tagName).toBe('HEADER');
    expect(header).toHaveClass('ds-card__header');
  });

  test('supports custom className', () => {
    render(
      <Card>
        <Card.Header className="custom-header">Header</Card.Header>
      </Card>
    );
    
    expect(screen.getByText('Header')).toHaveClass('custom-header');
  });

  test('forwards ref correctly', () => {
    const ref = React.createRef();
    render(
      <Card>
        <Card.Header ref={ref}>Header</Card.Header>
      </Card>
    );
    
    expect(ref.current).toBeInstanceOf(HTMLElement);
  });
});

describe('Card.Title', () => {
  test('renders card title with default level', () => {
    render(
      <Card>
        <Card.Title>Card Title</Card.Title>
      </Card>
    );
    
    const title = screen.getByRole('heading', { level: 3 });
    expect(title).toHaveTextContent('Card Title');
    expect(title).toHaveClass('ds-card__title');
  });

  test('renders different heading levels', () => {
    const { rerender } = render(
      <Card>
        <Card.Title level={1}>H1 Title</Card.Title>
      </Card>
    );
    expect(screen.getByRole('heading', { level: 1 })).toHaveTextContent('H1 Title');
    
    rerender(
      <Card>
        <Card.Title level={2}>H2 Title</Card.Title>
      </Card>
    );
    expect(screen.getByRole('heading', { level: 2 })).toHaveTextContent('H2 Title');
  });

  test('supports custom className', () => {
    render(
      <Card>
        <Card.Title className="custom-title">Title</Card.Title>
      </Card>
    );
    
    expect(screen.getByRole('heading')).toHaveClass('custom-title');
  });

  test('forwards ref correctly', () => {
    const ref = React.createRef();
    render(
      <Card>
        <Card.Title ref={ref}>Title</Card.Title>
      </Card>
    );
    
    expect(ref.current).toBeInstanceOf(HTMLHeadingElement);
  });
});

describe('Card.Subtitle', () => {
  test('renders card subtitle', () => {
    render(
      <Card>
        <Card.Subtitle>Subtitle content</Card.Subtitle>
      </Card>
    );
    
    const subtitle = screen.getByText('Subtitle content');
    expect(subtitle.tagName).toBe('P');
    expect(subtitle).toHaveClass('ds-card__subtitle');
  });

  test('supports custom className', () => {
    render(
      <Card>
        <Card.Subtitle className="custom-subtitle">Subtitle</Card.Subtitle>
      </Card>
    );
    
    expect(screen.getByText('Subtitle')).toHaveClass('custom-subtitle');
  });

  test('forwards ref correctly', () => {
    const ref = React.createRef();
    render(
      <Card>
        <Card.Subtitle ref={ref}>Subtitle</Card.Subtitle>
      </Card>
    );
    
    expect(ref.current).toBeInstanceOf(HTMLParagraphElement);
  });
});

describe('Card.Body', () => {
  test('renders card body', () => {
    render(
      <Card>
        <Card.Body>Body content</Card.Body>
      </Card>
    );
    
    const body = screen.getByText('Body content');
    expect(body.tagName).toBe('DIV');
    expect(body).toHaveClass('ds-card__body');
  });

  test('supports custom className', () => {
    render(
      <Card>
        <Card.Body className="custom-body">Body</Card.Body>
      </Card>
    );
    
    expect(screen.getByText('Body')).toHaveClass('custom-body');
  });

  test('forwards ref correctly', () => {
    const ref = React.createRef();
    render(
      <Card>
        <Card.Body ref={ref}>Body</Card.Body>
      </Card>
    );
    
    expect(ref.current).toBeInstanceOf(HTMLDivElement);
  });
});

describe('Card.Footer', () => {
  test('renders card footer', () => {
    render(
      <Card>
        <Card.Footer>Footer content</Card.Footer>
      </Card>
    );
    
    const footer = screen.getByText('Footer content');
    expect(footer.tagName).toBe('FOOTER');
    expect(footer).toHaveClass('ds-card__footer');
  });

  test('supports custom className', () => {
    render(
      <Card>
        <Card.Footer className="custom-footer">Footer</Card.Footer>
      </Card>
    );
    
    expect(screen.getByText('Footer')).toHaveClass('custom-footer');
  });

  test('forwards ref correctly', () => {
    const ref = React.createRef();
    render(
      <Card>
        <Card.Footer ref={ref}>Footer</Card.Footer>
      </Card>
    );
    
    expect(ref.current).toBeInstanceOf(HTMLElement);
  });
});

describe('Card.Actions', () => {
  test('renders card actions with default alignment', () => {
    render(
      <Card>
        <Card.Actions>
          <button>Action</button>
        </Card.Actions>
      </Card>
    );
    
    const actions = screen.getByText('Action').closest('.ds-card__actions');
    expect(actions).toHaveClass('ds-card__actions', 'ds-card__actions--end');
  });

  test('renders different alignments', () => {
    const { rerender } = render(
      <Card>
        <Card.Actions align="start">
          <button>Action</button>
        </Card.Actions>
      </Card>
    );
    expect(screen.getByText('Action').closest('.ds-card__actions')).toHaveClass('ds-card__actions--start');
    
    rerender(
      <Card>
        <Card.Actions align="center">
          <button>Action</button>
        </Card.Actions>
      </Card>
    );
    expect(screen.getByText('Action').closest('.ds-card__actions')).toHaveClass('ds-card__actions--center');
  });

  test('supports custom className', () => {
    render(
      <Card>
        <Card.Actions className="custom-actions">
          <button>Action</button>
        </Card.Actions>
      </Card>
    );
    
    expect(screen.getByText('Action').closest('.ds-card__actions')).toHaveClass('custom-actions');
  });

  test('forwards ref correctly', () => {
    const ref = React.createRef();
    render(
      <Card>
        <Card.Actions ref={ref}>
          <button>Action</button>
        </Card.Actions>
      </Card>
    );
    
    expect(ref.current).toBeInstanceOf(HTMLDivElement);
  });
});

describe('Card composition', () => {
  test('renders complete card structure', () => {
    render(
      <Card>
        <Card.Header>
          <Card.Title>Card Title</Card.Title>
          <Card.Subtitle>Card Subtitle</Card.Subtitle>
        </Card.Header>
        <Card.Body>
          <p>Card body content</p>
        </Card.Body>
        <Card.Footer>
          <Card.Actions>
            <button>Cancel</button>
            <button>Save</button>
          </Card.Actions>
        </Card.Footer>
      </Card>
    );
    
    expect(screen.getByRole('heading', { level: 3 })).toHaveTextContent('Card Title');
    expect(screen.getByText('Card Subtitle')).toBeInTheDocument();
    expect(screen.getByText('Card body content')).toBeInTheDocument();
    expect(screen.getByRole('button', { name: 'Cancel' })).toBeInTheDocument();
    expect(screen.getByRole('button', { name: 'Save' })).toBeInTheDocument();
  });
});