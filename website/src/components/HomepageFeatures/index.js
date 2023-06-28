import React from 'react';
import clsx from 'clsx';
import styles from './styles.module.css';

const FeatureList = [
    {
        title: 'Automate the boring stuff',
        Svg: require('@site/static/img/undraw_docusaurus_mountain.svg').default,
        description: (
            <>
                EY-ML-Template automates Python package creation and configuration
                with
                CI/CD. It's easy to use, even for developers unfamiliar with the
                tool. It handles the configuration automatically, freeing up
                time
                for developers to focus on their work.
            </>
        ),
    },
    {
        title: 'Focus on What Matters',
        Svg: require('@site/static/img/undraw_docusaurus_tree.svg').default,
        description: (
            <>
                EY-ML-Template simplifies the process of creating and configuring
                Python packages, allowing you to focus on developing and testing
                packages that meet your business needs. It saves you time and
                effort by handling the configuration and tools for you.
            </>
        ),
    },
    {
        title: 'Powered by Cookiecutter',
        Svg: require('@site/static/img/undraw_docusaurus_react.svg').default,
        description: (
            <>
                This project is built using Cookiecutter, a widely used tool
                among developers. It is easy to download and customize, making
                it a convenient choice for many developers.
            </>
        ),
    },
];

function Feature({Svg, title, description}) {
    return (
        <div className={clsx('col col--4')}>
            <div className="text--center">
                <Svg className={styles.featureSvg} role="img"/>
            </div>
            <div className="text--center padding-horiz--md">
                <h3>{title}</h3>
                <p>{description}</p>
            </div>
        </div>
    );
}

export default function HomepageFeatures() {
    return (
        <section className={styles.features}>
            <div className="container">
                <div className="row">
                    {FeatureList.map((props, idx) => (
                        <Feature key={idx} {...props} />
                    ))}
                </div>
            </div>
        </section>
    );
}
