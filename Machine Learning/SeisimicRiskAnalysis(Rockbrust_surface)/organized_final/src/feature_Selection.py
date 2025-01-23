from sklearn.feature_selection import SelectKBest, chi2
from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SequentialFeatureSelector
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import Lasso

def feature_selection(X,y,technique):
    if technique == "selectKbest":
        X_selected = SelectKBest(chi2, k=5).fit_transform(X, y)
        return X_selected
    elif technique == "RFE": ##  Recursive Feature Elimination (RFE)
        model = RandomForestClassifier()
        selector = RFE(model, n_features_to_select=5)
        X_selected = selector.fit_transform(X, y)
        return X_selected
    elif technique == "SFS": ##  Sequential Feature Selection (
        model = LogisticRegression()
        selector = SequentialFeatureSelector(model, n_features_to_select=5)
        X_selected = selector.fit_transform(X, y)
        return X_selected
    elif technique == "lasso":
        model = Lasso(alpha=0.01)
        model.fit(X, y)
        X_selected = X.loc[:, model.coef_ != 0]
        return X_selected
    elif technique == "randomforest":
        model = RandomForestClassifier()
        model.fit(X, y)
        feature_importance = model.feature_importances_
        important_features = X.columns[feature_importance > 0.02]
        X_selected = X[important_features]
        return X_selected