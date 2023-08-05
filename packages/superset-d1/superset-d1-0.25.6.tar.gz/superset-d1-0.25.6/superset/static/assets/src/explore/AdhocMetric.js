import { sqlaAutoGeneratedMetricRegex } from './constants';

export const EXPRESSION_TYPES = {
  SIMPLE: 'SIMPLE',
  SQL: 'SQL',
};

function inferSqlExpressionColumn(adhocMetric) {
  if (adhocMetric.sqlExpression && sqlaAutoGeneratedMetricRegex.test(adhocMetric.sqlExpression)) {
    const indexFirstCloseParen = adhocMetric.sqlExpression.indexOf(')');
    const indexPairedOpenParen =
      adhocMetric.sqlExpression.substring(0, indexFirstCloseParen).lastIndexOf('(');
    if (indexFirstCloseParen > 0 && indexPairedOpenParen > 0) {
      return adhocMetric.sqlExpression.substring(indexPairedOpenParen + 1, indexFirstCloseParen);
    }
  }
  return null;
}

function inferSqlExpressionAggregate(adhocMetric) {
  if (adhocMetric.sqlExpression && sqlaAutoGeneratedMetricRegex.test(adhocMetric.sqlExpression)) {
    const indexFirstOpenParen = adhocMetric.sqlExpression.indexOf('(');
    if (indexFirstOpenParen > 0) {
      return adhocMetric.sqlExpression.substring(0, indexFirstOpenParen);
    }
  }
  return null;
}

export default class AdhocMetric {
  constructor(adhocMetric) {
    this.expressionType = adhocMetric.expressionType || EXPRESSION_TYPES.SIMPLE;
    if (this.expressionType === EXPRESSION_TYPES.SIMPLE) {
      // try to be clever in the case of transitioning from Sql expression back to simple expression
      const inferredColumn = inferSqlExpressionColumn(adhocMetric);
      this.column = adhocMetric.column || (inferredColumn && { column_name: inferredColumn });
      this.aggregate = adhocMetric.aggregate || inferSqlExpressionAggregate(adhocMetric);
      this.sqlExpression = null;
    } else if (this.expressionType === EXPRESSION_TYPES.SQL) {
      this.sqlExpression = adhocMetric.sqlExpression;
      this.column = null;
      this.aggregate = null;
    }
    this.hasCustomLabel = !!(adhocMetric.hasCustomLabel && adhocMetric.label);
    this.fromFormData = !!adhocMetric.optionName;
    this.label = this.hasCustomLabel ? adhocMetric.label : this.getDefaultLabel();

    this.optionName = adhocMetric.optionName ||
      `metric_${Math.random().toString(36).substring(2, 15)}_${Math.random().toString(36).substring(2, 15)}`;
  }

  getDefaultLabel() {
    if (this.expressionType === EXPRESSION_TYPES.SIMPLE) {
      return `${this.aggregate || ''}(${(this.column && this.column.column_name) || ''})`;
    } else if (this.expressionType === EXPRESSION_TYPES.SQL) {
      return this.sqlExpression.length < 43 ?
        this.sqlExpression :
        this.sqlExpression.substring(0, 40) + '...';
    }
    return 'malformatted metric';
  }

  duplicateWith(nextFields) {
    return new AdhocMetric({
      ...this,
      ...nextFields,
    });
  }

  equals(adhocMetric) {
    return adhocMetric.label === this.label &&
      adhocMetric.expressionType === this.expressionType &&
      adhocMetric.sqlExpression === this.sqlExpression &&
      adhocMetric.aggregate === this.aggregate &&
      (
        (adhocMetric.column && adhocMetric.column.column_name) ===
        (this.column && this.column.column_name)
      );
  }

  isValid() {
    if (this.expressionType === EXPRESSION_TYPES.SIMPLE) {
      return !!(this.column && this.aggregate);
    } else if (this.expressionType === EXPRESSION_TYPES.SQL) {
      return !!(this.sqlExpression);
    }
    return false;
  }

  inferSqlExpressionAggregate() {
    return inferSqlExpressionAggregate(this);
  }

  inferSqlExpressionColumn() {
    return inferSqlExpressionColumn(this);
  }
}
