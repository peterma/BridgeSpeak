import React from 'react';
import { cn } from '../lib/utils';

/**
 * ResponsiveGrid - A utility component for creating responsive grid layouts
 * Uses Tailwind's mobile-first breakpoint system
 */
export const ResponsiveGrid = ({ 
  children, 
  cols = "1 sm:2 lg:3", 
  gap = "4 md:6",
  className,
  ...props 
}) => {
  return (
    <div 
      className={cn(
        "grid",
        `grid-cols-${cols.replace(/\s+/g, ' grid-cols-')}`,
        `gap-${gap.replace(/\s+/g, ' gap-')}`,
        className
      )}
      {...props}
    >
      {children}
    </div>
  );
};

/**
 * ResponsiveContainer - A utility component for responsive containers
 */
export const ResponsiveContainer = ({ 
  children, 
  size = "7xl",
  padding = "4 sm:6 lg:8",
  className,
  ...props 
}) => {
  return (
    <div 
      className={cn(
        `max-w-${size}`,
        "mx-auto",
        `px-${padding.replace(/\s+/g, ' px-')}`,
        className
      )}
      {...props}
    >
      {children}
    </div>
  );
};

/**
 * ResponsiveCard - A utility component for responsive cards
 */
export const ResponsiveCard = ({ 
  children, 
  padding = "4 md:6",
  className,
  ...props 
}) => {
  return (
    <div 
      className={cn(
        "bg-white rounded-lg border shadow-sm",
        `p-${padding.replace(/\s+/g, ' p-')}`,
        "transition-shadow hover:shadow-md",
        className
      )}
      {...props}
    >
      {children}
    </div>
  );
};

/**
 * ResponsiveText - A utility component for responsive typography
 */
export const ResponsiveText = ({ 
  children, 
  as: Component = "p",
  size = "base md:lg",
  weight = "normal",
  color = "gray-700",
  className,
  ...props 
}) => {
  return (
    <Component 
      className={cn(
        `text-${size.replace(/\s+/g, ' text-')}`,
        `font-${weight}`,
        `text-${color}`,
        className
      )}
      {...props}
    >
      {children}
    </Component>
  );
};